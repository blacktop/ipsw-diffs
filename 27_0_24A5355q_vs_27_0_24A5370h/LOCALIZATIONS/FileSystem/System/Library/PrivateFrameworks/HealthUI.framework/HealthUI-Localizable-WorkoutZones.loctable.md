## HealthUI

> `FileSystem/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI-Localizable-WorkoutZones.loctable`

```diff

 en.CYCLING_POWER_CONFIGURATION_AUTOMATIC_FOOTER = "Your Functional Threshold Power (FTP) is estimated based on your heart rate and power output during recent activities."
 en.CYCLING_POWER_CONFIGURATION_CANCEL = "Cancel"
 en.CYCLING_POWER_CONFIGURATION_EMPTY_ZONE_WATTS_RANGE = "—"
-en.CYCLING_POWER_CONFIGURATION_END_OF_ZONE_TITLE = "UPPER LIMIT"
+en.CYCLING_POWER_CONFIGURATION_END_OF_ZONE_TITLE = "Upper Limit"
 en.CYCLING_POWER_CONFIGURATION_FIRST_ZONE_WATTS_RANGE = "\u003c%1$@%2$@"
 en.CYCLING_POWER_CONFIGURATION_FTP_AVAILABLE_FORMAT = "%1$@%2$@"
 en.CYCLING_POWER_CONFIGURATION_FTP_EMPTY_VALUE = "—"

 en.CYCLING_POWER_CONFIGURATION_MANUAL_FOOTER = "A cycling power sensor must be connected to your Apple Watch via Bluetooth to record power data."
 en.CYCLING_POWER_CONFIGURATION_PANE_TITLE = "Cycling Power"
 en.CYCLING_POWER_CONFIGURATION_POWER_ZONES_SIZE_HEADER = "Power Zones"
-en.CYCLING_POWER_CONFIGURATION_POWER_ZONES_SIZE_ITEM_TITLE = "%ld Zones"
+en.CYCLING_POWER_CONFIGURATION_POWER_ZONES_SIZE_ITEM_TITLE.NSStringLocalizedFormatKey = "%#@zones@"
+en.CYCLING_POWER_CONFIGURATION_POWER_ZONES_SIZE_ITEM_TITLE.zones.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.CYCLING_POWER_CONFIGURATION_POWER_ZONES_SIZE_ITEM_TITLE.zones.NSStringFormatValueTypeKey = "ld"
+en.CYCLING_POWER_CONFIGURATION_POWER_ZONES_SIZE_ITEM_TITLE.zones.one = "%ld Zone"
+en.CYCLING_POWER_CONFIGURATION_POWER_ZONES_SIZE_ITEM_TITLE.zones.other = "%ld Zones"
 en.CYCLING_POWER_CONFIGURATION_RECALCULATE_ZONES_FOOTER = "This will recalculate your zones to the recommended values based on your FTP."
 en.CYCLING_POWER_CONFIGURATION_RECALCULATE_ZONES_TITLE = "Reset Zone Percentages"
-en.CYCLING_POWER_CONFIGURATION_START_OF_ZONE_TITLE = "LOWER LIMIT"
+en.CYCLING_POWER_CONFIGURATION_START_OF_ZONE_TITLE = "Lower Limit"
 en.CYCLING_POWER_CONFIGURATION_ZONE_PERCENTAGE_RANGE = "%1$@–%2$@%%"
 en.CYCLING_POWER_CONFIGURATION_ZONE_TITLE = "Zone %ld"
 en.CYCLING_POWER_CONFIGURATION_ZONE_WATTS_RANGE = "%1$@–%2$@%3$@"

 en.HEART_RATE_CONFIGURATION_AUTOMATIC_FOOTER = "Automatic heart rate zones are calculated using the heart rate reserve method. Max and resting heart rate values are updated on the first of every month."
 en.HEART_RATE_CONFIGURATION_AUTOMATIC_NO_DOB_FOOTER = "For automatic heart rate zones, set your date of birth in Health Details."
 en.HEART_RATE_CONFIGURATION_BEATS_PER_MINUTE = "Beats per Minute"
-en.HEART_RATE_CONFIGURATION_END_OF_ZONE_TITLE = "UPPER LIMIT"
+en.HEART_RATE_CONFIGURATION_END_OF_ZONE_TITLE = "Upper Limit"
 en.HEART_RATE_CONFIGURATION_FIRST_ZONE_MANUAL_VALUE = "\u003c%@"
 en.HEART_RATE_CONFIGURATION_LAST_ZONE_MANUAL_VALUE = "%@+"
 en.HEART_RATE_CONFIGURATION_MANUAL = "Manual"

 en.HEART_RATE_CONFIGURATION_MAXIMUM_TITLE = "Maximum"
 en.HEART_RATE_CONFIGURATION_PANE_TITLE = "Heart Rate"
 en.HEART_RATE_CONFIGURATION_RESTING_TITLE = "Resting"
-en.HEART_RATE_CONFIGURATION_START_OF_ZONE_TITLE = "LOWER LIMIT"
-en.HEART_RATE_CONFIGURATION_ZONES_TITLE = "HEART RATE ZONES"
+en.HEART_RATE_CONFIGURATION_START_OF_ZONE_TITLE = "Lower Limit"
+en.HEART_RATE_CONFIGURATION_ZONES_TITLE = "Heart Rate Zones"
 en.HEART_RATE_CONFIGURATION_ZONE_DETAIL = "Zone %ld"
 en.HEART_RATE_CONFIGURATION_ZONE_MANUAL_VALUE = "%1$@–%2$@"
+en.WORKOUT_CYCLING_POWER_CONFIGURATION_AUTOMATIC_FTP_NOT_AVAILABLE_FOOTER = "To see your estimated functional threshold power (FTP) and power zones, first ensure your date of birth, height, and weight are entered in Health on your iPhone. Then, connect a cycling power meter to your Apple Watch using Bluetooth in settings. After about 5 high intensity rides with your power meter connected, your estimated FTP and power zones will be available."
+en.WORKOUT_CYCLING_POWER_CONFIGURATION_AUTOMATIC_FTP_NOT_AVAILABLE_NAME = "Automatic FTP and Power Zones"

```
