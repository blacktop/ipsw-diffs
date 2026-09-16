## HDSDiagnostics

> `/Applications/HDSViewService.app/PlugIns/HDSDiagnostics.appex/HDSDiagnostics`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-405.0.11.0.0
-  __TEXT.__text: 0xb9c
-  __TEXT.__auth_stubs: 0x1b0
-  __TEXT.__objc_stubs: 0x340
+405.10.26.0.0
+  __TEXT.__text: 0xc64
+  __TEXT.__auth_stubs: 0x1c0
+  __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x68
-  __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x115
-  __TEXT.__oslogstring: 0xb5
+  __TEXT.__const: 0x58
+  __TEXT.__cstring: 0x174
+  __TEXT.__oslogstring: 0x10f
   __TEXT.__objc_classname: 0x18
-  __TEXT.__objc_methname: 0x2a4
+  __TEXT.__objc_methname: 0x2d8
   __TEXT.__objc_methtype: 0x26
   __TEXT.__unwind_info: 0x90
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__cfstring: 0x1a0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xe0
+  __DATA_CONST.__auth_got: 0xe8
   __DATA_CONST.__got: 0x48
   __DATA.__objc_const: 0x90
-  __DATA.__objc_selrefs: 0xe8
+  __DATA.__objc_selrefs: 0x100
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 10
-  Symbols:   49
-  CStrings:  57
+  Symbols:   50
+  CStrings:  64
 
Symbols:
+ _objc_retain_x2
Functions:
~ sub_100001188 : 232 -> 432
CStrings:
+ "Consent not provided for sensitive attachment collection; skipping. Host app [%{public}@]"
+ "DEExtensionAttachmentsParamConsentProvidedKey"
+ "DEExtensionHostAppKey"
+ "boolValue"
+ "com.apple.enhancedloggingd"
+ "isEqualToString:"
+ "objectForKeyedSubscript:"
```
