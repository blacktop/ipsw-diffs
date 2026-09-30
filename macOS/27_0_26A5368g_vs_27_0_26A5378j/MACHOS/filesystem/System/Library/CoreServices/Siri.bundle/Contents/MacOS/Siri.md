## Siri

> `/System/Library/CoreServices/Siri.bundle/Contents/MacOS/Siri`

```diff

-  __TEXT.__text: 0x1298
+  __TEXT.__text: 0x13c0
   __TEXT.__auth_stubs: 0x130
-  __TEXT.__objc_stubs: 0x940
+  __TEXT.__objc_stubs: 0x900
   __TEXT.__objc_methlist: 0x118
   __TEXT.__const: 0x18
-  __TEXT.__cstring: 0x212
-  __TEXT.__objc_methname: 0x668
-  __TEXT.__oslogstring: 0xe7
+  __TEXT.__cstring: 0x230
+  __TEXT.__objc_methname: 0x64f
+  __TEXT.__oslogstring: 0x110
   __TEXT.__objc_classname: 0xf
-  __TEXT.__objc_methtype: 0xa1
+  __TEXT.__objc_methtype: 0x94
   __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__const: 0x90
   __DATA_CONST.__cfstring: 0x260

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__auth_got: 0xa0
-  __DATA_CONST.__got: 0xa8
-  __DATA.__objc_const: 0xf0
-  __DATA.__objc_selrefs: 0x298
-  __DATA.__objc_ivar: 0x8
+  __DATA_CONST.__got: 0xb0
+  __DATA.__objc_const: 0xb8
+  __DATA.__objc_selrefs: 0x290
+  __DATA.__objc_ivar: 0x4
   __DATA.__objc_data: 0x50
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   Functions: 27
   Symbols:   49
-  CStrings:  150
+  CStrings:  147
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA.__objc_data : content changed
CStrings:
+ "%s Got hardware menu long press invocation"
+ "%s Got hardware menu tap invocation"
+ "-[SiriStatusMenu _onLongPress:]"
+ "-[SiriStatusMenu _onTap:]"
+ "_launchOptionsForStatusItem"
+ "_onLongPress:"
+ "_onTap:"
+ "setLongPressAction:"
- "%s Got hardware menu press invocation"
- "-[SiriStatusMenu _onMouse:]"
- "B"
- "TB,V_ignoreMouseUp"
- "_ignoreMouseUp"
- "_onMouse:"
- "ignoreMouseUp"
- "sendActionOn:"
- "setIgnoreMouseUp:"
- "type"
- "v20@0:8B16"

```
