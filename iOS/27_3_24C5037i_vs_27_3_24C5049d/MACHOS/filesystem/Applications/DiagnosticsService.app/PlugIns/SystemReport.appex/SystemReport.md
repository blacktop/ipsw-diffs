## SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-1374.60.20.0.0
-  __TEXT.__text: 0x1e57c
+1374.60.29.0.0
+  __TEXT.__text: 0x1ee58
   __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_stubs: 0x44e0
-  __TEXT.__objc_methlist: 0x1d4c
-  __TEXT.__cstring: 0x3cc3
+  __TEXT.__objc_stubs: 0x45e0
+  __TEXT.__objc_methlist: 0x1d9c
+  __TEXT.__cstring: 0x3ce7
   __TEXT.__const: 0x98
-  __TEXT.__oslogstring: 0x2358
-  __TEXT.__objc_classname: 0x6de
+  __TEXT.__oslogstring: 0x2492
+  __TEXT.__objc_classname: 0x6ed
   __TEXT.__objc_methtype: 0x5c5
-  __TEXT.__objc_methname: 0x3659
+  __TEXT.__objc_methname: 0x3726
   __TEXT.__gcc_except_tab: 0x27c
-  __TEXT.__unwind_info: 0x930
-  __DATA_CONST.__const: 0x568
-  __DATA_CONST.__cfstring: 0x56c0
-  __DATA_CONST.__objc_classlist: 0x268
+  __TEXT.__unwind_info: 0x950
+  __DATA_CONST.__const: 0x5b0
+  __DATA_CONST.__cfstring: 0x5700
+  __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0xa8
   __DATA_CONST.__auth_got: 0x688
-  __DATA_CONST.__got: 0x258
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA.__objc_const: 0x35b0
-  __DATA.__objc_selrefs: 0x1330
+  __DATA.__objc_const: 0x3640
+  __DATA.__objc_selrefs: 0x1370
   __DATA.__objc_ivar: 0xa4
-  __DATA.__objc_data: 0x1810
+  __DATA.__objc_data: 0x1860
   __DATA.__data: 0xc0
   __DATA.__common: 0x10
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/HearingUtilities.framework/HearingUtilities
   - /System/Library/PrivateFrameworks/IOMobileFramebuffer.framework/IOMobileFramebuffer
   - /System/Library/PrivateFrameworks/MFAAuthentication.framework/MFAAuthentication
+  - /System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor
   - /System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation
   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 656
-  Symbols:   336
-  CStrings:  1735
+  Functions: 664
+  Symbols:   337
+  CStrings:  1751
 
Symbols:
+ _OBJC_CLASS_$_MSUDataAccessor
CStrings:
+ "AppleAuthCPRelay is RCAM: %d. Flags: %x."
+ "ComponentHinge"
+ "Failed to read hinge lifetime statistics: %@"
+ "Failed to resolve hinge data path: %@"
+ "Found hinge data path"
+ "No RCAM AuthCP relay present; skipping RCAM authentication attributes."
+ "Skipping hinge statistic '%@': value is not JSON serializable"
+ "[ERROR] BatteryQueryForConfig returned nil, unexpected class, or missing index for config array (batteryIndex: %ld, count: %lu)"
+ "copyPathForPersistentData:error:"
+ "initWithContentsOfURL:error:"
+ "lifetimeStatistics"
+ "path"
+ "populateRCAMAuthenticationStatus:"
+ "preferencesFileURL"
+ "rcamAuthValueForProperty:"
+ "sharedDataAccessor"
+ "statistics.plist"
+ "stringByAppendingPathComponent:"
- "[ERROR] BatteryQueryForConfig returned nil, unexpected class, or zero count for config array"
- "lastObject"
```
