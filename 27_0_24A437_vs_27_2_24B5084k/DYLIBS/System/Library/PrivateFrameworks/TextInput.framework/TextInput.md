## TextInput

> `/System/Library/PrivateFrameworks/TextInput.framework/TextInput`

```diff

-3567.0.0.0.0
-  __TEXT.__text: 0x7d4b8
-  __TEXT.__objc_methlist: 0xb660
+3568.1.4.0.0
+  __TEXT.__text: 0x7d738
+  __TEXT.__objc_methlist: 0xb680
   __TEXT.__dlopen_cstrs: 0x459
-  __TEXT.__const: 0x4b0
-  __TEXT.__cstring: 0x49636
+  __TEXT.__const: 0x4d0
+  __TEXT.__cstring: 0x4959c
   __TEXT.__ustring: 0xc8bc8
-  __TEXT.__oslogstring: 0x974
-  __TEXT.__unwind_info: 0x2a10
+  __TEXT.__oslogstring: 0xb19
+  __TEXT.__unwind_info: 0x2a18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x24a0
-  __DATA_CONST.__objc_classlist: 0x5b8
+  __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x56c0
+  __DATA_CONST.__objc_selrefs: 0x56c8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x400
-  __DATA_CONST.__objc_arraydata: 0x101948
+  __DATA_CONST.__objc_arraydata: 0x101a18
   __DATA_CONST.__got: 0x620
-  __AUTH_CONST.__const: 0xd60
-  __AUTH_CONST.__cfstring: 0x255d20
-  __AUTH_CONST.__objc_const: 0x11bd0
+  __AUTH_CONST.__const: 0xd80
+  __AUTH_CONST.__cfstring: 0x255d40
+  __AUTH_CONST.__objc_const: 0x11c60
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x5058
-  __AUTH_CONST.__objc_dictobj: 0xf190
-  __AUTH_CONST.__objc_intobj: 0xd38
+  __AUTH_CONST.__objc_arrayobj: 0x5070
+  __AUTH_CONST.__objc_dictobj: 0xf1b8
+  __AUTH_CONST.__objc_intobj: 0xd50
   __AUTH_CONST.__objc_doubleobj: 0xc0
   __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH.__objc_data: 0x2620
+  __AUTH.__objc_data: 0x2670
   __DATA.__objc_ivar: 0xb7c
   __DATA.__data: 0xc90
   __DATA_DIRTY.__objc_data: 0x1310

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4011
-  Symbols:   9341
-  CStrings:  76804
+  Functions: 4015
+  Symbols:   9353
+  CStrings:  76808
 
Symbols:
+ +[TIMecabraComposedCharacterCandidate supportsSecureCoding]
+ +[TIMecabraComposedCharacterCandidate type]
+ _OBJC_CLASS_$_TIMecabraComposedCharacterCandidate
+ _OBJC_METACLASS_$_TIMecabraComposedCharacterCandidate
+ _TIInputManagerClientOSLogFacility
+ _TIInputManagerClientOSLogFacility.logFacility
+ _TIInputManagerClientOSLogFacility.onceToken
+ __OBJC_$_CLASS_METHODS_TIMecabraComposedCharacterCandidate
+ __OBJC_CLASS_RO_$_TIMecabraComposedCharacterCandidate
+ __OBJC_METACLASS_RO_$_TIMecabraComposedCharacterCandidate
+ ___TIInputManagerClientOSLogFacility_block_invoke
+ _objc_msgSend$localizedDescription
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.2.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "IM Client closed connection to kbd (Please check for kbd crash logs.) after failures sending %{public}@. Last error domain=%{public}@ code=%{public}ld: %{public}@"
+ "IM Client falling back to stub input manager to handle request: %{public}@"
+ "IM Client intentionally invalidating connection to kbd"
+ "IM Client will retry (attempt %{public}ld) sending %{public}@ to kbd after error domain=%{public}@ code=%{public}ld: %{public}@"
+ "KBDInputManagerClient"
+ "Kurdish-Sorani-QWERTY"
+ "TIMecabraComposedCharacterCandidate"
- "%s will retry sending %@ to keyboard daemon after receiving %@"
- "-[TIKeyboardInputManagerClient handleError:forRequest:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1161: libc++ Hardening assertion __position != end() failed: vector::erase(iterator) called with a non-dereferenceable iterator\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS27.0.Internal.sdk/usr/include/c++/v1/__vector/vector.h:414: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
- "Please check for kbd crash logs. %s closed connection to keyboard daemon after two consecutive failures sending %@"
```
