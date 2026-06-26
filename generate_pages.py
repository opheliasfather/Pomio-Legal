#!/usr/bin/env python3
"""Generate Pomio legal HTML pages for all supported languages."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
LAST_UPDATED = "June 26, 2026"
BUNDLE_ID = "com.pomodoro.six11"
CONTACT = "support@six11apps.com"

LANGS: dict[str, dict] = {
    "en": {
        "name": "English",
        "dir": "ltr",
        "privacy_title": "Privacy Policy",
        "terms_title": "Terms of Use",
        "privacy_desc": "How Pomio handles your data",
        "terms_desc": "Rules for using the App",
        "privacy_body": [
            ("", "Welcome to Pomio. We value your privacy. Pomio is a Pomodoro-based productivity application designed to help you focus, manage tasks, and track your progress with custom themes and charts."),
            ("Data Collection", "Pomio runs locally. We do not collect, store, or share any personal identity data, calendar event contents, focus statistics, or custom tasks on external servers. All your data remains strictly on your device."),
            ("Analytics", "We may use minimal localized crash reports to ensure optimal performance. No behavioral tracking is executed."),
            ("Security", "Your focus data and routine configurations are secured by your operating system's native sandboxing capabilities."),
            ("Contact Us", f"If you have questions about this Privacy Policy, contact us at: {CONTACT}"),
        ],
        "terms_body": [
            ("", "By downloading or using Pomio, you agree to these Terms of Use."),
            ("Acceptance", "By downloading or using Pomio, you agree to these terms."),
            ("License", "We grant you a personal, non-transferable, revocable license to use the app for personal growth and productivity purposes."),
            ("Premium & Themes", "Any optional support or theme selection is managed securely through standard App Store purchase protocols."),
            ("Disclaimer", "Pomio is provided \"as is\" without warranty of any kind. We are not liable for any productivity loss or technical disruptions."),
        ],
    },
    "tr": {
        "name": "Türkçe",
        "dir": "ltr",
        "privacy_title": "Gizlilik Politikası",
        "terms_title": "Kullanım Şartları",
        "privacy_desc": "Pomio verilerinizi nasıl işler",
        "terms_desc": "Uygulama kullanım kuralları",
        "privacy_body": [
            ("", "Pomio'ya hoş geldiniz. Gizliliğinize önem veriyoruz. Pomio; odaklanmanıza, görevlerinizi yönetmenize, özel temalar ve grafiklerle ilerlemenizi takip etmenize yardımcı olan bir Pomodoro verimlilik uygulamasıdır."),
            ("Veri Toplama", "Pomio yerel olarak çalışır. Kişisel kimlik verilerinizi, takvim etkinliklerinizi, odaklanma istatistiklerinizi veya özel görevlerinizi harici sunucularda toplamıyoruz, saklamıyoruz veya paylaşmıyoruz. Tüm verileriniz kesinlikle cihazınızda kalır."),
            ("Analizler", "Uygulama çökme oranlarını izlemek ve optimum performansı sağlamak için minimum düzeyde yerelleştirilmiş hata raporları kullanabiliriz."),
            ("İletişim", f"Bu politika hakkında sorularınız için: {CONTACT}"),
        ],
        "terms_body": [
            ("", "Pomio'yu indirerek veya kullanarak bu şartları kabul etmiş sayılırsınız."),
            ("Kabul", "Pomio'yu indirerek veya kullanarak bu şartları kabul etmiş sayılırsınız."),
            ("Lisans", "Uygulamayı kişisel gelişim ve verimlilik amacıyla kullanmanız için size kişisel, devredilemez ve iptal edilebilir bir lisans veriyoruz."),
            ("Sorumluluk Reddi", "Pomio \"olduğu gibi\" sunulmaktadır. Herhangi bir verimlilik kaybı veya teknik aksaklıktan sorumlu değiliz."),
        ],
    },
    "fr": {
        "name": "Français",
        "dir": "ltr",
        "privacy_title": "Politique de Confidentialité",
        "terms_title": "Conditions d'Utilisation",
        "privacy_desc": "Comment Pomio traite vos données",
        "terms_desc": "Règles d'utilisation",
        "privacy_body": [
            ("", "Bienvenue sur Pomio. Nous apprécions votre vie privée. Pomio est une application de productivité basée sur la méthode Pomodoro pour gérer vos tâches et suivre vos statistiques."),
            ("Collecte de données", "Pomio fonctionne localement. Nous ne collectons ni ne partageons aucune donnée personnelle, tâche ou calendrier sur des serveurs externes. Toutes les données restent sur votre appareil."),
        ],
        "terms_body": [
            ("Acceptation", "En utilisant Pomio, vous acceptez les présentes conditions."),
            ("Utilisation", "L'application est fournie pour un usage personnel et non commercial."),
        ],
    },
    "de": {
        "name": "Deutsch",
        "dir": "ltr",
        "privacy_title": "Datenschutzerklärung",
        "terms_title": "Nutzungsbedingungen",
        "privacy_desc": "Datenschutz bei Pomio",
        "terms_desc": "Nutzungsregeln",
        "privacy_body": [
            ("", "Willkommen bei Pomio. Wir schätzen Ihre Privatsphäre. Pomio ist eine Pomodoro-Produktivitäts-App zur Verwaltung von Aufgaben und Fokus-Statistiken."),
            ("Datenerhebung", "Alle Daten verbleiben lokal auf Ihrem Gerät. Wir speichern keine persönlichen Daten oder Aufgaben auf externen Servern."),
        ],
        "terms_body": [
            ("Akzeptanz", "Mit der Nutzung von Pomio stimmen Sie diesen Bedingungen zu."),
            ("Haftungsausschluss", "Die Bereitstellung erfolgt ohne Gewährleistung."),
        ],
    },
    "es": {
        "name": "Español",
        "dir": "ltr",
        "privacy_title": "Política de Privacidad",
        "terms_title": "Términos de Servicio",
        "privacy_desc": "Privacidad en Pomio",
        "terms_desc": "Condiciones de uso",
        "privacy_body": [
            ("", "Bienvenido a Pomio. Respetamos su privacidad. Pomio funciona de forma local y no almacena datos de tareas, enfoque o calendario en servidores externos. Todos los datos permanecen en su dispositivo."),
        ],
        "terms_body": [
            ("Acuerdo", "Al usar la aplicación, usted acepta estos términos de uso y condiciones del servicio."),
            ("Uso", "La aplicación se proporciona para uso estrictamente personal."),
        ],
    },
    "pt": {
        "name": "Português",
        "dir": "ltr",
        "privacy_title": "Política de Privacidade",
        "terms_title": "Termos de Serviço",
        "privacy_desc": "Privacidade no Pomio",
        "terms_desc": "Termos de uso",
        "privacy_body": [
            ("", "Bem-vindo ao Pomio. Seus dados de foco, tarefas, calendário e estatísticas permanecem totalmente seguros no seu dispositivo local. Não coletamos informações externas."),
        ],
        "terms_body": [
            ("Termos", "O uso do aplicativo constitui aceitação integral destes termos de serviço."),
            ("Isenção de Responsabilidade", "O aplicativo é fornecido \"como está\" para produtividade."),
        ],
    },
    "zh": {
        "name": "中文",
        "dir": "ltr",
        "privacy_title": "隐私政策",
        "terms_title": "服务条款",
        "privacy_desc": "Pomio 隐私说明",
        "terms_desc": "使用条款",
        "privacy_body": [
            ("", "欢迎使用 Pomio。我们重视您的隐私。您的所有专注时间、任务、日历集成与统计数据均完全保存在本地设备中，不上传至任何外部服务器。"),
        ],
        "terms_body": [
            ("条款接受", "下载并使用本应用即表示您同意本服务条款。"),
            ("使用许可", "本应用仅供个人和非商业用途。"),
        ],
    },
    "ja": {
        "name": "日本語",
        "dir": "ltr",
        "privacy_title": "プライバシーポリシー",
        "terms_title": "利用規約",
        "privacy_desc": "Pomio のプライバシー",
        "terms_desc": "利用条件",
        "privacy_body": [
            ("", "Pomioへようこそ。ユーザーのタスク、カレンダー、集中データ、および統計はすべて外部サーバーへは送信されず、端末内に安全に保存されます。"),
        ],
        "terms_body": [
            ("同意", "本アプリを利用することで、これらの規約に同意したものとみなされます。"),
            ("免責事項", "本アプリは現状有姿で提供され、技術的な不具合について責任を負いません。"),
        ],
    },
    "ko": {
        "name": "한국어",
        "dir": "ltr",
        "privacy_title": "개인정보 처리방침",
        "terms_title": "이용약관",
        "privacy_desc": "Pomio 개인정보 안내",
        "terms_desc": "이용 조건",
        "privacy_body": [
            ("", "Pomio를 이용해 주셔서 감사합니다. 사용자의 모든 집중 통계, 작업, 일정 및 테마 설정 데이터는 외부 서버에 저장되지 않으며 로컬 기기에만 저장됩니다."),
        ],
        "terms_body": [
            ("동의", "앱을 다운로드하고 사용함으로써 본 이용약관에 동의하게 됩니다."),
            ("책임 제한", "본 앱은 \"있는 그대로\" 제공되며, 이용 중 발생한 손실에 대해 책임을 지지 않습니다."),
        ],
    },
    "ar": {
        "name": "العربية",
        "dir": "rtl",
        "privacy_title": "سياسة الخصوصية",
        "terms_title": "شروط الخدمة",
        "privacy_desc": "خصوصية Pomio",
        "terms_desc": "شروط الاستخدام",
        "privacy_body": [
            ("", "مرحباً بك في Pomio. نحن نحترم خصوصيتك. جميع البيانات الخاصة بالمهام، التقويم، وإحصاءات التركيز تحفظ محلياً بالكامل على جهازك ولا يتم مشاركتها مع أي خوادم خارجية."),
        ],
        "terms_body": [
            ("موافقة", "استخدام التطبيق يعني موافقتك الكاملة على شروط وأحكام الخدمة."),
            ("الترخيص", "نمنحك ترخيصاً شخصياً وغير قابل للتحويل لاستخدام التطبيق لزيادة الإنتاجية."),
        ],
    },
    "it": {
        "name": "Italiano",
        "dir": "ltr",
        "privacy_title": "Informativa sulla Privacy",
        "terms_title": "Termini di Servizio",
        "privacy_desc": "Privacy di Pomio",
        "terms_desc": "Condizioni d'uso",
        "privacy_body": [
            ("", "Benvenuto su Pomio. La tua privacy è la nostra priorità. I dati di focus, i task, il calendario e le statistiche rimangono esclusivamente sul tuo dispositivo locale."),
        ],
        "terms_body": [
            ("Accettazione", "L'uso dell'applicazione comporta l'accettazione integrale dei presenti termini."),
            ("Limitazione di responsabilità", "L'applicazione è fornita \"così com'è\" senza garanzie."),
        ],
    },
    "nl": {
        "name": "Nederlands",
        "dir": "ltr",
        "privacy_title": "Privacybeleid",
        "terms_title": "Algemene Voorwaarden",
        "privacy_desc": "Privacy bij Pomio",
        "terms_desc": "Gebruiksvoorwaarden",
        "privacy_body": [
            ("", "Welkom bij Pomio. Al uw focusstatistieken, taken, agendagegevens en persoonlijke voorkeuren worden lokaal op uw apparaat opgeslagen en niet gedeeld met externe servers."),
        ],
        "terms_body": [
            ("Acceptatie", "Door de app te gebruiken, gaat u akkoord met deze algemene voorwaarden."),
            ("Licentie", "U krijgt een persoonlijke, niet-overdraagbare licentie voor productiviteitsgebruik."),
        ],
    },
    "ru": {
        "name": "Русский",
        "dir": "ltr",
        "privacy_title": "Политика конфиденциальности",
        "terms_title": "Условия использования",
        "privacy_desc": "Конфиденциальность Pomio",
        "terms_desc": "Условия использования",
        "privacy_body": [
            ("", "Добро пожаловать в Pomio. Все ваши задачи, статистика фокуса, настройки тем и данные календаря сохраняются исключительно на вашем устройстве и не передаются на внешние сервера."),
        ],
        "terms_body": [
            ("Согласие", "Использование приложения означает полное согласие с данными условиями."),
            ("Отказ от ответственности", "Приложение предоставляется по принципу \"как есть\" для личного пользования."),
        ],
    },
    "hi": {
        "name": "हिन्दी",
        "dir": "ltr",
        "privacy_title": "गोपनीयता नीति",
        "terms_title": "सेवा की शर्तें",
        "privacy_desc": "Pomio गोपनीयता",
        "terms_desc": "उपयोग की शर्तें",
        "privacy_body": [
            ("", "Pomio में आपका स्वागत है। आपकी गोपनीयता हमारे लिए महत्वपूर्ण है। सभी कार्य, कैलेंडर इवेंट, फ़ोकस डेटा और सांख्यिकी आपके डिवाइस पर सुरक्षित रहते हैं और किसी बाहरी सर्वर पर नहीं भेजे जाते।"),
        ],
        "terms_body": [
            ("स्वीकृति", "इस ऐप का उपयोग करने पर आप इन सेवा शर्तों से पूरी तरह सहमत होते हैं।"),
            ("अस्वीकरण", "Pomio ऐप \"जैसा है\" वैसा ही प्रदान किया गया है, और हम किसी भी तकनीकी व्यवधान के लिए उत्तरदायी नहीं हैं।"),
        ],
    },
}


def css_href(lang_code: str) -> str:
    return "../style.css" if lang_code != "en" else "style.css"


def link_prefix(lang_code: str) -> str:
    return "../" if lang_code != "en" else ""


def render_body(sections: list[tuple[str, str]]) -> str:
    parts: list[str] = []
    mail_link = f'<a href="mailto:{CONTACT}">{CONTACT}</a>'
    for heading, text in sections:
        if heading:
            parts.append(f"      <h2>{heading}</h2>")
        if CONTACT in text:
            parts.append(f"      <p>{text.replace(CONTACT, mail_link)}</p>")
        else:
            parts.append(f"      <p>{text}</p>")
    return "\n".join(parts)


def render_doc(lang_code: str, doc: str) -> str:
    data = LANGS[lang_code]
    is_privacy = doc == "privacy"
    title = data["privacy_title"] if is_privacy else data["terms_title"]
    body = data["privacy_body"] if is_privacy else data["terms_body"]
    other = "terms-of-use.html" if is_privacy else "privacy-policy.html"
    other_label = data["terms_title"] if is_privacy else data["privacy_title"]
    prefix = link_prefix(lang_code)
    css = css_href(lang_code)
    dir_attr = f' dir="{data["dir"]}"' if data["dir"] == "rtl" else ""

    en_link = (
        '<span aria-hidden="true"> &middot; </span><a href="../privacy-policy.html">English</a>'
        if lang_code != "en"
        else ""
    )

    return f"""<!DOCTYPE html>
<html lang="{lang_code}"{dir_attr}>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Pomio</title>
  <meta name="description" content="{title} for Pomio, the lofi Pomodoro app by SIX11.">
  <link rel="stylesheet" href="{css}">
</head>
<body>
  <main class="page">
    <header class="header">
      <p class="eyebrow">Pomio</p>
      <h1>{title}</h1>
      <p class="meta">Last updated: {LAST_UPDATED}</p>
    </header>

    <article class="content">
{render_body(body)}
    </article>

    <footer class="footer">
      <a href="{prefix}{other}">{other_label}</a>
      <span aria-hidden="true"> &middot; </span>
      <a href="{prefix}index.html">Pomio Legal</a>
      {en_link}
    </footer>
  </main>
</body>
</html>
"""


def render_index() -> str:
  cards = []
  for code, data in LANGS.items():
    prefix = "" if code == "en" else f"{code}/"
    cards.append(
      f"""      <a class="card" href="{prefix}privacy-policy.html">
        <strong>{data['privacy_title']}</strong>
        <span>{data['name']}</span>
      </a>
      <a class="card" href="{prefix}terms-of-use.html">
        <strong>{data['terms_title']}</strong>
        <span>{data['name']}</span>
      </a>"""
    )
  grid = "\n".join(cards)
  return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Pomio — Legal</title>
  <meta name="description" content="Legal documents for Pomio lofi Pomodoro timer.">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="page">
    <header class="header">
      <p class="eyebrow">Pomio</p>
      <h1>Legal</h1>
      <p class="meta">Lofi Pomodoro timer for iOS</p>
    </header>

    <nav class="links lang-grid">
{grid}
    </nav>

    <footer class="footer">
      <p>&copy; 2026 SIX11 &middot; Bundle ID: {BUNDLE_ID}</p>
    </footer>
  </main>
</body>
</html>
"""


def main() -> None:
    (ROOT / "index.html").write_text(render_index(), encoding="utf-8")
    for code in LANGS:
        out_dir = ROOT if code == "en" else ROOT / code
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "privacy-policy.html").write_text(render_doc(code, "privacy"), encoding="utf-8")
        (out_dir / "terms-of-use.html").write_text(render_doc(code, "terms"), encoding="utf-8")
    print(f"Generated legal pages for {len(LANGS)} languages.")


if __name__ == "__main__":
    main()
