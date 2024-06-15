import requests
import argparse

plugins = (
    "jetpack",
    "akismet",
    "contact-form-7",
    "woocommerce",
    "wordfence",
    "yoast-seo",
    "elementor",
    "w3-total-cache",
    "updraftplus",
    "wpforms",
    "all-in-one-seo-pack",
    "google-analytics-for-wordpress",
    "really-simple-ssl",
    "wordfence-security",
    "classic-editor",
    "wpmu-dev-upfront",
    "wpmu-dev-vc-templating",
    "wpmu-dev-videopress",
    "wpmu-dev-wp-forminator",
    "revslider",
    "gravityforms",
    "wp-fastest-cache",
    "duplicator",
    "wordfence",
    "wordfence-security",
    "form-maker",
    "backwpup",
    "wp-file-manager",
    "easy-wp-smtp",
    "social-warfare",
    "wp-live-chat-support",
    "total-theme",
    "wp-super-cache",
    "visual-composer",
    "ultimate-member",
)

def check_plugin(base_url, plugin):
    url = f"{base_url}{plugin}/readme.txt"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def main():
    parser = argparse.ArgumentParser(description="Detecta plugins vulnerables en una instalación de WordPress.")
    parser.add_argument('domain', type=str, help='El dominio de la instalación de WordPress, por ejemplo, example.com')
    
    args = parser.parse_args()
    base_urls = [f"http://{args.domain}/wp-content/plugins/", f"https://{args.domain}/wp-content/plugins/"]

    found_plugins = []

    for base_url in base_urls:
        for plugin in plugins:
            if check_plugin(base_url, plugin):
                found_plugins.append(plugin)

    if found_plugins:
        print("[+] Plugins encontrados:")
        for plugin in found_plugins:
            print(f"    - {plugin}")
    else:
        print("[-] No se encontraron plugins vulnerables.")

if __name__ == "__main__":
    main()