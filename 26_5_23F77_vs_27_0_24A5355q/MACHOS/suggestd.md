## suggestd

> `/System/Library/PrivateFrameworks/CoreSuggestions.framework/suggestd`

```diff

-1311.7.0.0.0
-  __TEXT.__text: 0x2a9c
-  __TEXT.__auth_stubs: 0x5a0
-  __TEXT.__objc_stubs: 0xb80
-  __TEXT.__objc_methlist: 0xa34
-  __TEXT.__const: 0x88
-  __TEXT.__dlopen_cstrs: 0x6a
-  __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__cstring: 0x48f
-  __TEXT.__objc_methname: 0x24bb
-  __TEXT.__objc_classname: 0x31c
-  __TEXT.__objc_methtype: 0x157f
+1331.0.1.0.0
+  __TEXT.__text: 0x25fc
+  __TEXT.__auth_stubs: 0x580
+  __TEXT.__objc_stubs: 0xbe0
+  __TEXT.__objc_methlist: 0xa5c
+  __TEXT.__const: 0x80
+  __TEXT.__gcc_except_tab: 0xe0
+  __TEXT.__cstring: 0x47b
+  __TEXT.__objc_methname: 0x259b
+  __TEXT.__objc_classname: 0x315
+  __TEXT.__objc_methtype: 0x15c9
   __TEXT.__oslogstring: 0x308
   __TEXT.__unwind_info: 0x140
-  __DATA_CONST.__auth_got: 0x2e0
-  __DATA_CONST.__got: 0x170
-  __DATA_CONST.__const: 0x190
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__linkguard: 0xe
-  __DATA.__objc_const: 0xb48
-  __DATA.__objc_selrefs: 0x7f8
+  __DATA_CONST.__auth_got: 0x2d0
+  __DATA_CONST.__got: 0x188
+  __DATA.__objc_const: 0xb60
+  __DATA.__objc_selrefs: 0x828
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0x140
   __DATA.__data: 0x7e0
-  __DATA.__bss: 0x28
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/ProactiveExperimentsInternals.framework/ProactiveExperimentsInternals
   - /System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting
   - /System/Library/PrivateFrameworks/ProactiveInputPredictionsInternals.framework/ProactiveInputPredictionsInternals
+  - /System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/appleinternal/lib/liblinkguard.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: A728C0FF-A6F2-36C6-B1A2-45286004FFAC
-  Functions: 50
-  Symbols:   148
-  CStrings:  544
+  UUID: 00BC7EF2-A180-36A2-BA1B-BFB3EC6CF30D
+  Functions: 48
+  Symbols:   149
+  CStrings:  550
 
Symbols:
+ _OBJC_CLASS_$_PSUSummarizationPipeline
+ _OBJC_CLASS_$_PSUSummarizationXPCServer
+ _OBJC_CLASS_$_SGContactStoreFactory
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x8
- __Block_object_dispose
- __sl_dlopen
- _objc_autorelease
- _objc_getClass
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
- _objc_retain_x25
CStrings:
+ "contactMatchesWithContacts:limitTo:withCompletion:"
+ "contactStore"
+ "initWithContactStore:"
+ "nameForDetail:prependMaybe:onlySignificant:withCompletion:"
+ "requiredContactKeysForContactMatchingWithCompletion:"
+ "setSummarizationReceiver:"
+ "v40@0:8@\"NSString\"16B24B28@?<v@?@\"SGXPCResponse1\">32"
+ "v40@0:8@16B24B28@?32"
- "PSUSummarizationXPCServer"
- "softlink:o:path:/System/Library/PrivateFrameworks/ProactiveSummarization.framework/ProactiveSummarization"

```
