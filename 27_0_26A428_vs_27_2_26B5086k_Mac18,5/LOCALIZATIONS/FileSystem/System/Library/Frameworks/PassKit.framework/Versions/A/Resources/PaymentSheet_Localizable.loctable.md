## PassKit

> `FileSystem/System/Library/Frameworks/PassKit.framework/Versions/A/Resources/PaymentSheet_Localizable.loctable`

```diff

 en.PAYMENT_PASSWORD_PROMPT_FORMAT = "Enter the password for the user “%@” to complete this purchase."
 en.PAYMENT_PAY_BUTTON_TITLE = "Pay"
 en.PAYMENT_SHEET_ADD_AMOUNT_FMT = "Add %@"
+en.PAYMENT_SHEET_AMOUNT_AND_DURATION_FMT.Comment = "$1: interval (for localization only, not to be displayed to user), $2: amount (e.g $3.99, £1.05), $3: localized string from PAYMENT_SHEET_FOR_WITH_INTERVAL_FMT (e.g `per month`, `for 2 days`, `every 3 months for 12 months`). Final copy examples: `$3.99 per month for 3 months`, `$3.99 every 2 weeks for 12 weeks`, `$3.99 for 2 months`"
 en.PAYMENT_SHEET_AMOUNT_AND_DURATION_FMT.NSStringLocalizedFormatKey = "%1$#@period@"
 en.PAYMENT_SHEET_AMOUNT_AND_DURATION_FMT.period.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.PAYMENT_SHEET_AMOUNT_AND_DURATION_FMT.period.NSStringFormatValueTypeKey = "lu"
 en.PAYMENT_SHEET_AMOUNT_AND_DURATION_FMT.period.other = "%2$@ %3$@"
 en.PAYMENT_SHEET_ENDING_DATE_FMT = "Ending %@"
+en.PAYMENT_SHEET_FOR_FMT.Comment = "[used only when interval == 1]. $1: localized string from NSDateComponentsFormatter (2 days, 3 months). Final copy: `for 3 months`"
 en.PAYMENT_SHEET_FOR_FMT.NSStringLocalizedFormatKey = "%#@period@"
 en.PAYMENT_SHEET_FOR_FMT.period.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.PAYMENT_SHEET_FOR_FMT.period.NSStringFormatValueTypeKey = "lu"
 en.PAYMENT_SHEET_FOR_FMT.period.other = "for %1$@"
+en.PAYMENT_SHEET_FOR_WITH_INTERVAL_FMT.Comment = "[used only when interval greater than 1]. $1: interval (for localization only, not to be displayed to user), $2: localized interval, $3: localized string from NSDateComponentsFormatter (2 days, 3 months). Final copy examples: `per month for 3 months`, `every 2 weeks for 12 weeks`"
 en.PAYMENT_SHEET_FOR_WITH_INTERVAL_FMT.NSStringLocalizedFormatKey = "%1$#@period@"
 en.PAYMENT_SHEET_FOR_WITH_INTERVAL_FMT.period.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.PAYMENT_SHEET_FOR_WITH_INTERVAL_FMT.period.NSStringFormatValueTypeKey = "lu"
 en.PAYMENT_SHEET_FOR_WITH_INTERVAL_FMT.period.other = "%2$@ for %3$@"
+en.PAYMENT_SHEET_FREE_TRIAL_FMT.Comment = "$1: localized interval string from NSDateComponentsFormatter (7 day, 1 month). Final copy examples: `7 day free trial`, `1 month free trial`"
 en.PAYMENT_SHEET_FREE_TRIAL_FMT.NSStringLocalizedFormatKey = "%#@period@"
 en.PAYMENT_SHEET_FREE_TRIAL_FMT.period.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.PAYMENT_SHEET_FREE_TRIAL_FMT.period.NSStringFormatValueTypeKey = "lu"
 en.PAYMENT_SHEET_FREE_TRIAL_FMT.period.other = "%1$@ free trial"
 en.PAYMENT_SHEET_ITEM_FREE_STANDALONE = "Free"
+en.PAYMENT_SHEET_ITEM_FREE_WITH_TIMING_FMT.Comment = "[used only when interval greater than 1]. $1: interval (for localization only, not to be displayed to user), $2: localized string from NSDateComponentsFormatter (2 days, 3 months). Final copy examples: `7 days free`, `4 months free`"
 en.PAYMENT_SHEET_ITEM_FREE_WITH_TIMING_FMT.NSStringLocalizedFormatKey = "%1$#@period@"
 en.PAYMENT_SHEET_ITEM_FREE_WITH_TIMING_FMT.period.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.PAYMENT_SHEET_ITEM_FREE_WITH_TIMING_FMT.period.NSStringFormatValueTypeKey = "lu"

 en.PAYMENT_SHEET_PENDING_AMOUNT_SUMMARY_ITEM = "…"
 en.PAYMENT_SHEET_STARTING_DATE_FMT = "Starting %@"
 en.PAYMENT_SHEET_STARTING_NOW = "Starting Now"
+en.PAYMENT_SHEET_TRIAL_FMT.Comment = "$1: localized interval string from NSDateComponentsFormatter (7 day, 1 month). Final copy examples: `7 day trial`, `1 month trial`"
 en.PAYMENT_SHEET_TRIAL_FMT.NSStringLocalizedFormatKey = "%#@period@"
 en.PAYMENT_SHEET_TRIAL_FMT.period.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
 en.PAYMENT_SHEET_TRIAL_FMT.period.NSStringFormatValueTypeKey = "lu"

```
