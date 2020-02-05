#!/usr/bin/env bash

set -o errexit
set -o nounset

urlencode() {
    # urlencode <string>
    old_lc_collate=${LC_COLLATE:-}
    LC_COLLATE=C

    local length="${#1}"
    for (( i = 0; i < length; i++ )); do
        local c="${1:i:1}"
        case $c in
            [a-zA-Z0-9.~_-]) printf "$c" ;;
            ' ') printf "%%20" ;;
            *) printf '%%%02X' "'$c" ;;
        esac
    done

    LC_COLLATE=$old_lc_collate
}

enc_db_user="$(urlencode "${DB_USER:-}")"
enc_db_password="$(urlencode "${DB_PASSWORD:-}")"
enc_db_database="$(urlencode "${DB_DATABASE:-}")"

: "${DB_URL:=postgresql://$enc_db_user:$enc_db_password@$DB_HOST:$DB_PORT/$enc_db_database}"
export DB_URL

exec "$@"
