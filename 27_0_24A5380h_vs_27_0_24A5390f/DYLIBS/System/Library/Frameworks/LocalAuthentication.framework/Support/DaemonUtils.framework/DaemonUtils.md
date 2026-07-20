## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-2319.0.33.0.1
-  __TEXT.__text: 0x8aa8
-  __TEXT.__objc_methlist: 0x1230
-  __TEXT.__const: 0x170
-  __TEXT.__cstring: 0x553
-  __TEXT.__oslogstring: 0x997
+2319.0.46.0.0
+  __TEXT.__text: 0x89d4
+  __TEXT.__objc_methlist: 0x1220
+  __TEXT.__const: 0x160
+  __TEXT.__cstring: 0x52d
+  __TEXT.__oslogstring: 0x96d
   __TEXT.__gcc_except_tab: 0xd0
   __TEXT.__unwind_info: 0x3a0
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c8
+  __DATA_CONST.__const: 0x1a0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_selrefs: 0xae8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x228
-  __AUTH_CONST.__const: 0x1e0
+  __DATA_CONST.__got: 0x238
+  __AUTH_CONST.__const: 0x1c0
   __AUTH_CONST.__cfstring: 0x5e0
-  __AUTH_CONST.__objc_const: 0x2b00
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__objc_const: 0x2b20
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2c0
-  __DATA.__objc_ivar: 0x160
+  __AUTH_CONST.__auth_got: 0x2b8
+  __DATA.__objc_ivar: 0x164
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__bss: 0xc8
+  __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 335
+  Functions: 331
   Symbols:   1002
-  CStrings:  114
+  CStrings:  109
 
Symbols:
+ -[LAAnalytics initWithEventName:reporter:]
+ GCC_except_table12
+ _LACDTOFeatureEnablementModeRawValueNotSet
+ _OBJC_CLASS_$_LACAnalyticsReporter
+ _OBJC_IVAR_$_LAAnalytics._reporter
+ _objc_msgSend$enablementMode
+ _objc_msgSend$initWithEventName:reporter:
+ _objc_msgSend$sendEventWithName:payload:
- -[LAAnalytics logLevel]
- -[LAAnalyticsDTO logLevel]
- GCC_except_table13
- GCC_except_table18
- _AnalyticsSendEventLazy
- ___23-[LAAnalytics _collect]_block_invoke
- ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
- _objc_msgSend$logLevel
CStrings:
- "%{public}s analytics event %{public}@: %@"
- "@\"NSDictionary\"8@?0"
- "C"
- "didn't send"
- "sent"
```
