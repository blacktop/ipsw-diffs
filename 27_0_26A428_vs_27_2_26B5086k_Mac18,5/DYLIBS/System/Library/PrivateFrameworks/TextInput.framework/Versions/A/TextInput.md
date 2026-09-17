## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/Versions/A/TextInput`

```diff

-3567.400.0.0.0
-  __TEXT.__text: 0x81a70
-  __TEXT.__objc_methlist: 0xb608
+3568.1.4.0.0
+  __TEXT.__text: 0x81d14
+  __TEXT.__objc_methlist: 0xb628
   __TEXT.__dlopen_cstrs: 0x1ea
-  __TEXT.__const: 0x4c0
-  __TEXT.__cstring: 0x49226
+  __TEXT.__const: 0x4d0
+  __TEXT.__cstring: 0x4918c
   __TEXT.__ustring: 0xc8bc8
-  __TEXT.__oslogstring: 0x974
-  __TEXT.__unwind_info: 0x2900
+  __TEXT.__oslogstring: 0xb19
+  __TEXT.__unwind_info: 0x2908
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x15c0
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x55f8
+  __DATA_CONST.__objc_selrefs: 0x5600
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x400
-  __DATA_CONST.__objc_arraydata: 0x101948
+  __DATA_CONST.__objc_arraydata: 0x101a18
   __DATA_CONST.__got: 0x608
-  __AUTH_CONST.__const: 0x1f50
-  __AUTH_CONST.__cfstring: 0x255b00
-  __AUTH_CONST.__objc_const: 0x11b78
+  __AUTH_CONST.__const: 0x1f70
+  __AUTH_CONST.__cfstring: 0x255b20
+  __AUTH_CONST.__objc_const: 0x11c08
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x5058
-  __AUTH_CONST.__objc_dictobj: 0xf190
-  __AUTH_CONST.__objc_intobj: 0xd08
+  __AUTH_CONST.__objc_arrayobj: 0x5070
+  __AUTH_CONST.__objc_dictobj: 0xf1b8
+  __AUTH_CONST.__objc_intobj: 0xd20
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__auth_got: 0x6b0
-  __AUTH.__objc_data: 0x2530
+  __AUTH.__objc_data: 0x2580
   __DATA.__objc_ivar: 0xb74
   __DATA.__data: 0xc90
   __DATA_DIRTY.__objc_data: 0x1400

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4015
-  Symbols:   9246
-  CStrings:  76768
+  Functions: 4019
+  Symbols:   9258
+  CStrings:  76772
 
Symbols:
+ +[TIMecabraComposedCharacterCandidate supportsSecureCoding]
+ +[TIMecabraComposedCharacterCandidate type]
+ TIInputManagerClientOSLogFacility.logFacility
+ TIInputManagerClientOSLogFacility.onceToken
+ _OBJC_CLASS_$_TIMecabraComposedCharacterCandidate
+ _OBJC_METACLASS_$_TIMecabraComposedCharacterCandidate
+ _TIInputManagerClientOSLogFacility
+ __OBJC_$_CLASS_METHODS_TIMecabraComposedCharacterCandidate
+ __OBJC_CLASS_RO_$_TIMecabraComposedCharacterCandidate
+ __OBJC_METACLASS_RO_$_TIMecabraComposedCharacterCandidate
+ ___TIInputManagerClientOSLogFacility_block_invoke
+ _objc_msgSend$localizedDescription
CStrings:
+ "IM Client closed connection to kbd (Please check for kbd crash logs.) after failures sending %{public}@. Last error domain=%{public}@ code=%{public}ld: %{public}@"
+ "IM Client falling back to stub input manager to handle request: %{public}@"
+ "IM Client intentionally invalidating connection to kbd"
+ "IM Client will retry (attempt %{public}ld) sending %{public}@ to kbd after error domain=%{public}@ code=%{public}ld: %{public}@"
+ "KBDInputManagerClient"
+ "Kurdish-Sorani-QWERTY"
+ "TIMecabraComposedCharacterCandidate"
- "%s will retry sending %@ to keyboard daemon after receiving %@"
- "-[TIKeyboardInputManagerClient handleError:forRequest:]"
- "Please check for kbd crash logs. %s closed connection to keyboard daemon after two consecutive failures sending %@"
```
