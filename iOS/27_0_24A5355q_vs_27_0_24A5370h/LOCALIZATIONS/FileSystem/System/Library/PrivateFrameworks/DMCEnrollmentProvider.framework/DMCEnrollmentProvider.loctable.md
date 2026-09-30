## DMCEnrollmentProvider

> `FileSystem/System/Library/PrivateFrameworks/DMCEnrollmentProvider.framework/DMCEnrollmentProvider.loctable`

```diff

 en.DMC_CONFIGURATIONS_TITLE = "Configurations"
 en.DMC_CONSENT_NOTICE = "Consent Notice"
 en.DMC_CONSENT_NOTICES = "Consent Notices"
-en.DMC_CONSENT_NOTICES_%@ = "%@ Consent Notices"
+en.DMC_CONSENT_NOTICES_%lu.NSStringLocalizedFormatKey = "%#@notices@"
+en.DMC_CONSENT_NOTICES_%lu.notices.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.DMC_CONSENT_NOTICES_%lu.notices.NSStringFormatValueTypeKey = "lu"
+en.DMC_CONSENT_NOTICES_%lu.notices.other = "%1$lu Consent Notices"
 en.DMC_CONTAINS_TITLE = "Contains"
 en.DMC_DESCRIPTION_TITLE = "Description"
 en.DMC_DEVICE_CONFIGURATIONS_TITLE = "Device Configurations"

```
