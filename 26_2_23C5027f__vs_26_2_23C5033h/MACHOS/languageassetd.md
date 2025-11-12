## languageassetd

> `/usr/libexec/languageassetd`

```diff

-64.0.0.0.0
-  __TEXT.__text: 0x3778
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_stubs: 0xb60
-  __TEXT.__objc_methlist: 0x1e8
-  __TEXT.__const: 0x20
-  __TEXT.__cstring: 0x6b6
-  __TEXT.__objc_methname: 0x920
+64.3.1.0.0
+  __TEXT.__text: 0x3db8
+  __TEXT.__auth_stubs: 0x460
+  __TEXT.__objc_stubs: 0xc40
+  __TEXT.__objc_methlist: 0x248
+  __TEXT.__const: 0x18
+  __TEXT.__cstring: 0x71b
+  __TEXT.__objc_methname: 0xa6a
   __TEXT.__oslogstring: 0x83
   __TEXT.__objc_classname: 0x2e
-  __TEXT.__objc_methtype: 0x102
-  __TEXT.__gcc_except_tab: 0x1c
-  __TEXT.__unwind_info: 0x118
-  __DATA_CONST.__auth_got: 0x208
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x2e0
-  __DATA_CONST.__cfstring: 0x840
+  __TEXT.__objc_methtype: 0x12f
+  __TEXT.__unwind_info: 0x130
+  __DATA_CONST.__auth_got: 0x238
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x358
+  __DATA_CONST.__cfstring: 0x860
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA.__objc_const: 0x1e8
-  __DATA.__objc_selrefs: 0x308
-  __DATA.__objc_ivar: 0x18
+  __DATA.__objc_const: 0x230
+  __DATA.__objc_selrefs: 0x340
+  __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0xa0
   __DATA.__bss: 0x30
   __DATA.__common: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AA51D88E-B234-323D-9655-8A4DEB425504
-  Functions: 58
-  Symbols:   99
-  CStrings:  267
+  UUID: 8A181F54-E17A-34C8-924D-BFBFD7D9AD46
+  Functions: 68
+  Symbols:   104
+  CStrings:  282
 
Symbols:
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_create
+ _dispatch_release
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_sync
+ _objc_release_x21
+ _objc_release_x22
- _OBJC_CLASS_$_NSDate
- __Unwind_Resume
- ___objc_personality_v0
- _objc_release_x24
CStrings:
+ "@\"NSObject<OS_dispatch_queue>\""
+ "Asset query timed out after 30 seconds"
+ "Catalog download failed. Error=%ld"
+ "_eventQueue"
+ "_synchronizationQueueForNeedsRedownload"
+ "array"
+ "com.apple.languageassetd.events"
+ "com.apple.languageassetd.sync"
+ "configureDictionaryDownloadFlags:languageAssetInfo:"
+ "configureDownloadFlagsForAssets:languageAssetInfo:assetType:"
+ "copy"
+ "handleCatalogDownloadResultForAssetType:languageAssetInfo:"
+ "initWithObjectsAndKeys:"
+ "needsRedownload"
+ "processDictionaryAssets:uniqueDictionaries:"
+ "processLanguageAssetInfo:"
+ "setNeedsRedownload:"
+ "startDownloadsForAssets:languageAssetInfo:assetType:"
+ "v32@0:8@16@24"
- "Catelog download failed. Error=%ld"
- "currentRunLoop"
- "dateWithTimeIntervalSinceNow:"
- "dictionaryWithObject:forKey:"
- "runUntilDate:"

```
