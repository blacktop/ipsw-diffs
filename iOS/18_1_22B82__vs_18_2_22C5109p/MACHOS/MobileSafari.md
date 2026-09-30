## MobileSafari

> `/System/Library/DataClassMigrators/MobileSafari.migrator/MobileSafari`

```diff

-7619.2.8.10.7
-  __TEXT.__text: 0x662c
-  __TEXT.__auth_stubs: 0x430
-  __TEXT.__objc_stubs: 0x1400
-  __TEXT.__objc_methlist: 0x244
+7620.1.11.10.8
+  __TEXT.__text: 0x6948
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_stubs: 0x1460
+  __TEXT.__objc_methlist: 0x25c
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__cstring: 0xcc1
-  __TEXT.__oslogstring: 0xf33
+  __TEXT.__cstring: 0xcc5
+  __TEXT.__oslogstring: 0x10c0
   __TEXT.__objc_classname: 0x58
-  __TEXT.__objc_methname: 0x1389
+  __TEXT.__objc_methname: 0x1402
   __TEXT.__objc_methtype: 0x18d
-  __TEXT.__unwind_info: 0x180
-  __DATA_CONST.__auth_got: 0x228
-  __DATA_CONST.__got: 0x2a8
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__auth_got: 0x230
+  __DATA_CONST.__got: 0x2b0
   __DATA_CONST.__const: 0x360
   __DATA_CONST.__cfstring: 0xec0
   __DATA_CONST.__objc_classlist: 0x10

   __DATA_CONST.__objc_arraydata: 0x128
   __DATA_CONST.__objc_arrayobj: 0xf0
   __DATA.__objc_const: 0x540
-  __DATA.__objc_selrefs: 0x568
+  __DATA.__objc_selrefs: 0x580
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0
   __DATA.__data: 0xc0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 103
-  Symbols:   215
-  CStrings:  421
+  Functions: 105
+  Symbols:   217
+  CStrings:  429
 
Symbols:
+ _OBJC_CLASS_$_UIWebClip
+ __os_feature_enabled_impl
CStrings:
+ "Attempting to ensure web clip placeholder bundles if needed"
+ "If this is unexpected, please run `mobile_install rebuild all` and reboot. See 20813516 for details."
+ "Safari does not appear to have a container path set. Datamigrator is about to exit. This is expected if Safari is not installed on the system."
+ "Skipped most of MobileSafari DataMigration due to not finding MobileSafari's container path."
+ "_ensureWebClipPlaceholderBundleIfNeeded"
+ "_safariContainerPathExists"
+ "clipsIncludingWebClips:includingAppClips:"
+ "ensurePlaceholderBundle"
+ "safari_browserSharedDefaults"
+ "safari_setShouldAutomaticallyDownloadReadingListItems:"
+ "wap"
- "_sf_safariDefaults"
- "_sf_safariSharedDefaults"
- "_sf_setShouldAutomaticallyDownloadReadingListItems:"

```
