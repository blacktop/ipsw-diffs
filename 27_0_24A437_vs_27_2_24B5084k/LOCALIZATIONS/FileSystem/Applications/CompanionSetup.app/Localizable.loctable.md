## CompanionSetup

> `FileSystem/Applications/CompanionSetup.app/Localizable.loctable`

```diff

 en.AUTHENTICATION_THROTTLED_DETAIL.value.one = "Incorrect authentication code. Try again in %lld second."
 en.AUTHENTICATION_THROTTLED_DETAIL.value.other = "Incorrect authentication code. Try again in %lld seconds."
 en.AUTHENTICATION_TITLE = "Pairing Code"
-en.CHANGE_SIRI_LANGUAGE = "Change Siri Language"
+en.CHANGE_SIRI_LANGUAGE.NSStringDeviceSpecificRuleType.ipad = "Change iPad Siri Language"
+en.CHANGE_SIRI_LANGUAGE.NSStringDeviceSpecificRuleType.other = "Change iPhone Siri Language"
 en.CHECK_HOME_NAME_SUBTITLE_CONFLICT = "A home with a similar name already exists. Try entering a different name."
 en.CHECK_HOME_NAME_SUBTITLE_ENDLETTER = "Names must start and end with a letter or number."
 en.CHECK_HOME_NAME_SUBTITLE_PROHIBITED_CHARACTER = "Names cannot contain special characters or emoji. Try a new name."

 en.UNSUPPORTED_LANGUAGE_MISMATCH_SECONDARY_SUBTITLE.NSStringDeviceSpecificRuleType.other = "The language you’re using for Siri on this iPhone does not match the language set for this {ProductName}.\n\nTo use Siri for personal content on this {ProductName}, change your iPhone Siri language to %@."
 en.UNSUPPORTED_LANGUAGE_MISMATCH_SECONDARY_TITLE.NSStringDeviceSpecificRuleType.ipad = "Change iPad Siri Language"
 en.UNSUPPORTED_LANGUAGE_MISMATCH_SECONDARY_TITLE.NSStringDeviceSpecificRuleType.other = "Change iPhone Siri Language"
-en.UNSUPPORTED_LANGUAGE_PRIMARY_ACTION_TITLE = "Choose Language"
-en.UNSUPPORTED_LANGUAGE_SUBTITLE_MATCHING.NSStringDeviceSpecificRuleType.ipad = "The language you’re using for Siri on this iPad is not available on {ProductName}.\n\nTo use Siri for personal content on {ProductName}, change your iPad Siri language to match the one you choose for {ProductName}."
-en.UNSUPPORTED_LANGUAGE_SUBTITLE_MATCHING.NSStringDeviceSpecificRuleType.other = "The language you’re using for Siri on this iPhone is not available on {ProductName}.\n\nTo use Siri for personal content on {ProductName}, change your iPhone Siri language to match the one you choose for {ProductName}."
-en.UNSUPPORTED_LANGUAGE_SUBTITLE_NOT_MATCHING.NSStringDeviceSpecificRuleType.ipad = "The languages you’re using for Siri and your iPad are not available on {ProductName}.\n\nTo use Siri for personal content on {ProductName}, change your iPad Siri language to match the one you choose for {ProductName}."
+en.UNSUPPORTED_LANGUAGE_PRIMARY_ACTION_TITLE = "Choose {ProductName} Language"
+en.UNSUPPORTED_LANGUAGE_SUBTITLE_NOT_MATCHING.NSStringDeviceSpecificRuleType.ipad = "The languages you’re using for Siri and your iPad are not available on {ProductName}. You can choose a different language for Siri and your iPad to one that {ProductName} supports. \n\nTo use Siri for personal content, all languages must match."
 en.UNSUPPORTED_LANGUAGE_SUBTITLE_NOT_MATCHING.NSStringDeviceSpecificRuleType.other = "The languages you’re using for Siri and your iPhone are not available on {ProductName}.\n\nTo use Siri for personal content on {ProductName}, change your iPhone Siri language to match the one you choose for {ProductName}."
-en.UNSUPPORTED_LANGUAGE_SUBTITLE_SIRI = "To get your personal content and use Siri with {ProductName}, you’ll need to change your Siri language."
-en.UNSUPPORTED_LANGUAGE_TITLE_MATCHING = "%@ Not Available"
+en.UNSUPPORTED_LANGUAGE_SUBTITLE_SIRI.NSStringDeviceSpecificRuleType.ipad = "The Siri language on your iPad is not available on {ProductName}. You can choose a different language for {ProductName}, or change the Siri language on your iPad to one that {ProductName} supports.\n\nTo use Siri for personal content, both languages must match."
+en.UNSUPPORTED_LANGUAGE_SUBTITLE_SIRI.NSStringDeviceSpecificRuleType.other = "The Siri language on your iPhone is not available on {ProductName}. You can choose a different language for {ProductName}, or change the Siri language on your iPhone to one that {ProductName} supports.\n\nTo use Siri for personal content, both languages must match."
 en.UNSUPPORTED_LANGUAGE_TITLE_NOT_MATCHING = "%@ and %@ Not Available"
 en.UNSUPPORTED_LANGUAGE_TITLE_SIRI = "%@ Not Available"
 en.UPDATE = "Update"

```
