## FindMyAppCore

> `FileSystem/private/var/staged_system_apps/FindMy.app/Frameworks/FindMyAppCore.framework/LocationSharing.loctable`

```diff

 en.LOCATION_SHARING_ERROR_ALERT_TITLE = "Error"
 en.LOCATION_SHARING_ERROR_SHARING_LOCATION_ALERT_TITLE = "Error Sharing Location"
 en.LOCATION_SHARING_ERROR_UPDATING_DEVICE_ALERT_TITLE = "Error Updating Me Device"
-en.LOCATION_SHARING_FOOTER_OFF_ACTIVE = "Sharing is suspended. Turn on Share My Location in the Me tab to restore your sharing settings."
-en.LOCATION_SHARING_FOOTER_OFF_INACTIVE = "Sharing is suspended. Turn on Share My Location in the Me tab to start sharing."
+en.LOCATION_SHARING_FOOTER_OFF_ACTIVE = "No one can see your location while Share My Location is off. Turn it on in the Me tab to restore your previous settings."
+en.LOCATION_SHARING_FOOTER_OFF_INACTIVE_%@ = "Share My Location is off. Turn it on in the Me tab to start sharing with %@."
+en.LOCATION_SHARING_FOOTER_OFF_INACTIVE_GENERIC = "Share My Location is off. Turn it on in the Me tab to start sharing with this person."
 en.LOCATION_SHARING_FROM_OTHER_DEVICE_AUTOME_%@ = "%@ and cellular Apple Watches"
 en.LOCATION_SHARING_FROM_THIS_DEVICE.NSStringDeviceSpecificRuleType.ipad = "This iPad"
 en.LOCATION_SHARING_FROM_THIS_DEVICE.NSStringDeviceSpecificRuleType.iphone = "This iPhone"

 en.LOCATION_SHARING_INDIVIDUALLY_PAUSED_ALERT_ACTION = "OK"
 en.LOCATION_SHARING_INDIVIDUALLY_PAUSED_ALERT_MESSAGE = "Sharing is back on, but people you chose to hide from won’t see your location until hiding ends."
 en.LOCATION_SHARING_INDIVIDUALLY_PAUSED_ALERT_TITLE = "You Remain Hidden from Some People"
+en.LOCATION_SHARING_INFO_SHEET_DETAIL_%@ = "Your location is shared from %@.\n\nIt switches automatically to the active device."
+en.LOCATION_SHARING_INFO_SHEET_DETAIL_WITH_WATCHES_%@ = "Your location is shared from %@ and cellular Apple Watches.\n\nIt switches automatically to the active device."
 en.LOCATION_SHARING_MENU_ITEM_SHARE_CUSTOM_DURATION = "Custom"
 en.LOCATION_SHARING_MENU_ITEM_SHARE_END_OF_DAY = "For Today"
 en.LOCATION_SHARING_MENU_ITEM_SHARE_INDEFINITELY = "Always"

 en.LOCATION_SHARING_STATUS_DURATION_INDEFINITELY = "Always sharing"
 en.LOCATION_SHARING_STATUS_DURATION_MINUTES_%@ = "Sharing for %@ min"
 en.LOCATION_SHARING_STATUS_DURATION_TIME_%@ = "Sharing until %@"
-en.LOCATION_SHARING_STATUS_DURATION_TOMORROW_%@ = "Sharing until tomorrow at %@"
+en.LOCATION_SHARING_STATUS_DURATION_TOMORROW_%@_%lld.NSStringLocalizedFormatKey = "%2$#@arg1@"
+en.LOCATION_SHARING_STATUS_DURATION_TOMORROW_%@_%lld.arg1.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.LOCATION_SHARING_STATUS_DURATION_TOMORROW_%@_%lld.arg1.NSStringFormatValueTypeKey = "lld"
+en.LOCATION_SHARING_STATUS_DURATION_TOMORROW_%@_%lld.arg1.one = "Sharing until tomorrow at %1$@"
+en.LOCATION_SHARING_STATUS_DURATION_TOMORROW_%@_%lld.arg1.other = "Sharing until tomorrow at %1$@"
 en.LOCATION_SHARING_STATUS_HIDING_ENDED = "Hiding ended"
 en.LOCATION_SHARING_STATUS_HIDING_MINUTES_%@ = "Hiding for %@ min"
 en.LOCATION_SHARING_STATUS_HIDING_TIME_%@ = "Hiding until %@"
 en.LOCATION_SHARING_STATUS_PAUSED = "Hiding"
-en.LOCATION_SHARING_STATUS_PAUSED_FOR_TODAY_%@ = "Hiding until tomorrow at %@"
+en.LOCATION_SHARING_STATUS_PAUSED_FOR_TODAY_%@_%lld.NSStringLocalizedFormatKey = "%2$#@arg1@"
+en.LOCATION_SHARING_STATUS_PAUSED_FOR_TODAY_%@_%lld.arg1.NSStringFormatSpecTypeKey = "NSStringPluralRuleType"
+en.LOCATION_SHARING_STATUS_PAUSED_FOR_TODAY_%@_%lld.arg1.NSStringFormatValueTypeKey = "lld"
+en.LOCATION_SHARING_STATUS_PAUSED_FOR_TODAY_%@_%lld.arg1.one = "Hiding until tomorrow at %1$@"
+en.LOCATION_SHARING_STATUS_PAUSED_FOR_TODAY_%@_%lld.arg1.other = "Hiding until tomorrow at %1$@"
 en.LOCATION_SHARING_STATUS_SHARING_ENDED = "Sharing ended"
 en.LOCATION_SHARING_TURN_OFF_ALERT_MESSAGE = "No one in Find My or Messages will see your location. People you share with won’t know you turned it off or back on."
 en.LOCATION_SHARING_TURN_OFF_ALERT_NOT_NOW_ACTION = "Not Now"

```
