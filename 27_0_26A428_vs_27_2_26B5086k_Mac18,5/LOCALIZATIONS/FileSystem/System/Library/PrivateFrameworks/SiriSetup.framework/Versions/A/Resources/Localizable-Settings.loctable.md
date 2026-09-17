## SiriSetup

> `FileSystem/System/Library/PrivateFrameworks/SiriSetup.framework/Versions/A/Resources/Localizable-Settings.loctable`

```diff

 en.LANGUAGE_ROW_TITLE = "Language"
 en.MAIN_PLACARD_SUBTITLE_AI.NSStringDeviceSpecificRuleType.mac = "Siri helps you get things done, just by asking. [Learn more…](help://com.apple.helpviewer?bookid=com.apple.machelp\u0026topicid=mchl6b029310)"
 en.MAIN_PLACARD_SUBTITLE_AI.NSStringDeviceSpecificRuleType.other = "Siri helps you get things done, just by asking. [Learn more…](learn-more://open?id=apple-intelligence)"
-en.MAIN_PLACARD_SUBTITLE_CLASSIC = "Siri is an intelligent assistant that helps you find information and get things done."
+en.MAIN_PLACARD_SUBTITLE_CLASSIC.NSStringDeviceSpecificRuleType.mac = "Siri is an intelligent assistant that helps you find information and get things done. [Learn more…](help://com.apple.helpviewer?bookid=com.apple.machelp\u0026topicid=mchl6b029310)"
+en.MAIN_PLACARD_SUBTITLE_CLASSIC.NSStringDeviceSpecificRuleType.other = "Siri is an intelligent assistant that helps you find information and get things done. [Learn more…](learn-more://open?id=siri)"
 en.MAIN_PLACARD_SUBTITLE_LINWOOD.NSStringDeviceSpecificRuleType.mac = "Powered by Apple Intelligence. You can have rich conversations, take advantage of more personal assistance, and get more done just by asking. [Learn more…](help://com.apple.helpviewer?bookid=com.apple.machelp\u0026topicid=mac88e1mkh19)"
 en.MAIN_PLACARD_SUBTITLE_LINWOOD.NSStringDeviceSpecificRuleType.other = "Powered by Apple Intelligence. You can have rich conversations, take advantage of more personal assistance, and get more done just by asking. [Learn more…](learn-more://open?id=enhanced-siri)"
 en.MAIN_PLACARD_VIEW_TITLE = "Siri"
 en.MAIN_PLACARD_VIEW_TITLE_CHINA_AI = "Apple Intelligence \u0026 Siri"
 en.MAIN_SECTION_PRIVACY_FOOTER = "Voice recordings and transcripts are sent to Apple for improvement purposes. [About Siri, Dictation \u0026 Privacy…](https://siri.privacy)"
 en.MAIN_SECTION_PRIVACY_FOOTER_OPTED_OUT = "Voice input is processed on %@. [About Siri, Dictation \u0026 Privacy…](https://siri.privacy)"
-en.MODELS_ENABLED_STATUS = "%1$lld enabled"
+en.MODELS_ENABLED_STATUS.NSStringLocalizedFormatKey = "%#@value@"
+en.MODELS_ENABLED_STATUS.value.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.MODELS_ENABLED_STATUS.value.NSStringFormatValueTypeKey = "lld"
+en.MODELS_ENABLED_STATUS.value.one = "%1$lld enabled"
+en.MODELS_ENABLED_STATUS.value.other = "%1$lld enabled"
 en.MODELS_ROW_TITLE = "Extensions"
 en.MY_INFO_ROW_TITLE = "Your Information"
 en.PERSONAL_SECTION_FOOTER = "Voice recordings and transcripts are sent to Apple for improvement purposes. [About Improve Siri \u0026 Privacy](https://siri.privacy)"

```
