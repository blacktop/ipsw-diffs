## MailAccountSettings

> `FileSystem/System/Library/PreferenceBundles/AccountSettings/MailAccountSettings.bundle/AccountPreferences.loctable`

```diff

 en.DOMAIN_SETUP_VIEW_INSTRUCTION_ON_WEB_LINK = "Open Instructions on the Web"
 en.DOMAIN_SETUP_VIEW_INSTRUCTION_ON_WEB_URL = "https://support.apple.com/kb/HT212524"
 en.DOMAIN_SETUP_VIEW_INSTRUCTION_PAGE_DESCRIPTION = "Copy these records exactly, including any ending punctuation, to make sure your emails are directed to iCloud Mail."
-en.DOMAIN_SETUP_VIEW_INSTRUCTION_PAGE_FOOTER = "Note: If your registrar doesn’t support “@” enter your domain name as the host. Start by including the period at the end of the MX and DKIM values and quotes in the SPF TXT record. If it fails, try entering the values without the quotes or without the ending punctuation."
 en.DOMAIN_SETUP_VIEW_INSTRUCTION_PAGE_HEADER = "View Instructions and Records"
+en.DOMAIN_SETUP_VIEW_INSTRUCTION_TIPS_TITLE = "Tips:"
+en.DOMAIN_SETUP_VIEW_INSTRUCTION_TIP_1 = "If your registrar doesn’t support “@” for the host, use your domain name instead."
+en.DOMAIN_SETUP_VIEW_INSTRUCTION_TIP_2 = "Copy the MX and DKIM values exactly, including the trailing period."
+en.DOMAIN_SETUP_VIEW_INSTRUCTION_TIP_3 = "Copy the SPF value exactly, including the quotation marks."
+en.DOMAIN_SETUP_VIEW_INSTRUCTION_TIP_4 = "If a record fails to save, try removing the trailing period and/or quotation marks."
 en.DONE = "Done"
 en.DRAFTS_MAILBOX = "Drafts Mailbox"
 en.EDIT = "Edit"

```
