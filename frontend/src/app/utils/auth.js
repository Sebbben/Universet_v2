import { makeParamsString } from "./general";

export function redirectToAuthLogin(router, redirect_uri="http://localhost:3000") {

    const params = {
        "response_type": "code",
        "client_id": "22b03b67-8b81-4bd8-8252-5415b90f45b2",
        "redirect_uri": redirect_uri,
        "state": "TODO"
    }

    router.push("http://auth.localhost:3000/login?" + makeParamsString(params));
}