## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-605.75.0.0.0
-  __TEXT.__text: 0x83018
+605.79.0.0.0
+  __TEXT.__text: 0x83158
   __TEXT.__auth_stubs: 0xf20
   __TEXT.__objc_stubs: 0x8160
   __TEXT.__objc_methlist: 0x2d70
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x127b4
+  __TEXT.__cstring: 0x127cc
   __TEXT.__gcc_except_tab: 0x4cfc
   __TEXT.__objc_methname: 0xc87d
-  __TEXT.__oslogstring: 0x11ffb
+  __TEXT.__oslogstring: 0x1215c
   __TEXT.__objc_classname: 0x33b
   __TEXT.__objc_methtype: 0x1097
   __TEXT.__dlopen_cstrs: 0x17a

   __DATA_CONST.__auth_got: 0x7a8
   __DATA_CONST.__got: 0x370
   __DATA_CONST.__const: 0x1198
-  __DATA_CONST.__cfstring: 0xfc80
+  __DATA_CONST.__cfstring: 0xfca0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/libsqlite3.dylib
   Functions: 1211
   Symbols:   372
-  CStrings:  5794
+  CStrings:  5798
 
CStrings:
+ "\"WiFiAnalytics_executables-605.79\""
+ "%!{(MISSING)public}s::%!d(MISSING):Alloc AnalyticsProcessor with AnalyticsProcessorMigrationCapable"
+ "%!{(MISSING)public}s::%!d(MISSING):Got keyBagLockStateChangeNotification isKeyBagUnlocked is true, attempting setup setupAnalyticsProcessorWithCompletionBlock"
+ "%!{(MISSING)public}s::%!d(MISSING):Result for triggerDeviceAnalyticsStoreMigrationAndReply via XPC - Error: WAErrorCodeKeyBagLocked. KeyBag not unlocked"
+ "%!{(MISSING)public}s::%!d(MISSING):Unable to alloc analyticsProcessor. Will not be processing any metrics for AnalyticsStore!"
+ "%!{(MISSING)public}s::%!d(MISSING):[WAUtil shouldEnableXPCStore] true, also etting AnalyticsProcessorEnableXPCStore"
+ "%!{(MISSING)public}s::%!d(MISSING):isKeyBagUnlocked is true, attempting setup setupAnalyticsProcessorWithCompletionBlock"
+ "Jul  8 2024 19:53:24"
+ "WAErrorCodeKeyBagLocked"
+ "WiFiAnalytics_executables-605.79"
- "\"WiFiAnalytics_executables-605.75\""
- "%!{(MISSING)public}s::%!d(MISSING):Readying AnalyticsProcessor after first unlock"
- "%!{(MISSING)public}s::%!d(MISSING):Result for triggerDeviceAnalyticsStoreMigrationAndReply via XPC - Error: WAErrorCodeFileSystemError. KeyBag not unlocked"
- "%!{(MISSING)public}s::%!d(MISSING):Unable to get analyticsProcessor. Will not be processing any metrics for AnalyticsStore!"
- "Jun 28 2024 12:37:05"
- "WiFiAnalytics_executables-605.75"

```
