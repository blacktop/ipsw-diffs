## TextInput_ar

> `/System/Library/TextInput/TextInput_ar.bundle/TextInput_ar`

```diff

-3504.100.0.0.0
-  __TEXT.__text: 0x7cc
-  __TEXT.__auth_stubs: 0x210
+3508.0.0.0.0
+  __TEXT.__text: 0x31c
+  __TEXT.__auth_stubs: 0x120
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x8c
+  __TEXT.__objc_methlist: 0x40
   __TEXT.__const: 0x8
-  __TEXT.__cstring: 0xa7
+  __TEXT.__cstring: 0xa0
   __TEXT.__ustring: 0x70
-  __TEXT.__objc_classname: 0x1c
-  __TEXT.__objc_methname: 0x27f
-  __TEXT.__objc_methtype: 0x5e
-  __TEXT.__objc_stubs: 0x200
-  __DATA_CONST.__got: 0x20
-  __DATA_CONST.__const: 0x50
+  __TEXT.__objc_classname: 0x1a
+  __TEXT.__objc_methname: 0xf6
+  __TEXT.__objc_methtype: 0x10
+  __TEXT.__objc_stubs: 0x100
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb0
+  __DATA_CONST.__objc_selrefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x1c0
-  __AUTH_CONST.__auth_got: 0x110
-  __AUTH_CONST.__cfstring: 0x760
-  __AUTH_CONST.__objc_const: 0x100
+  __AUTH_CONST.__auth_got: 0x98
+  __AUTH_CONST.__cfstring: 0x740
+  __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x8
   __DATA.__data: 0x28
-  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/TextInput.framework/TextInput

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A8423E15-2703-3AF0-8509-12A4AC252233
-  Functions: 15
-  Symbols:   104
-  CStrings:  128
+  UUID: 13FE5DBE-8EA3-35BD-A356-28397FE55F33
+  Functions: 7
+  Symbols:   57
+  CStrings:  104
 
Symbols:
+ +[TIKeyboardInputManager_ar generateKeyLayoutMapReverse]
+ +[TIKeyboardInputManager_ar generateKeyLayoutMap]
+ __OBJC_$_CLASS_METHODS_TIKeyboardInputManager_ar
+ ___56+[TIKeyboardInputManager_ar generateKeyLayoutMapReverse]_block_invoke
+ _objc_msgSend$generateKeyLayoutMap
- -[TIKeyboardInputManager_ar .cxx_destruct]
- -[TIKeyboardInputManager_ar initWithConfig:keyboardState:]
- -[TIKeyboardInputManager_ar initializeKeyLayoutMaps]
- -[TIKeyboardInputManager_ar internalStringToExternal:]
- -[TIKeyboardInputManager_ar internalStringToExternal:ignoreCompositionDisabled:]
- -[TIKeyboardInputManager_ar internalStringToSecondaryExternal:]
- -[TIKeyboardInputManager_ar keyLayoutMapReverse]
- -[TIKeyboardInputManager_ar keyLayoutMap]
- -[TIKeyboardInputManager_ar validUSetForAutocorrectionSecondary]
- OBJC_IVAR_$_TIKeyboardInputManager.m_impl
- _OBJC_IVAR_$_TIKeyboardInputManager_ar._keyLayoutMap
- _OBJC_IVAR_$_TIKeyboardInputManager_ar._keyLayoutMapReverse
- __OBJC_$_INSTANCE_VARIABLES_TIKeyboardInputManager_ar
- __OBJC_$_PROP_LIST_TIKeyboardInputManager_ar
- __ZN2KB6StringD1Ev
- __ZN2KB9ns_stringERKNS_6StringE
- __ZNK14TIInputManager12input_stringEv
- __ZNK14TIInputManager12is_uppercaseEj
- __ZZ64-[TIKeyboardInputManager_ar validUSetForAutocorrectionSecondary]E10onceToken2
- __ZZ64-[TIKeyboardInputManager_ar validUSetForAutocorrectionSecondary]E13secondary_set
- ___52-[TIKeyboardInputManager_ar initializeKeyLayoutMaps]_block_invoke
- ___64-[TIKeyboardInputManager_ar validUSetForAutocorrectionSecondary]_block_invoke
- ___block_descriptor_40_a8_32s_e5_v8?0ls32l8
- ___stack_chk_fail
- ___stack_chk_guard
- _dispatch_once
- _objc_msgSend$choseSecondary
- _objc_msgSend$hasPrefix:
- _objc_msgSend$initializeKeyLayoutMaps
- _objc_msgSend$internalStringToExternal:ignoreCompositionDisabled:
- _objc_msgSend$internalStringToSecondaryExternal:
- _objc_msgSend$keyLayoutMap
- _objc_msgSend$length
- _objc_msgSend$stringByAppendingString:
- _objc_msgSend$substringWithRange:
- _objc_release_x20
- _objc_release_x25
- _objc_release_x26
- _objc_release_x27
- _objc_release_x28
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x21
- _objc_retain_x26
- _objc_storeStrong
CStrings:
+ "generateKeyLayoutMap"
+ "generateKeyLayoutMapReverse"
- ""
- ".cxx_destruct"
- "@\"NSDictionary\""
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8@16@24"
- "T@\"NSDictionary\",R,N,V_keyLayoutMap"
- "T@\"NSDictionary\",R,N,V_keyLayoutMapReverse"
- "^{USet=}16@0:8"
- "_keyLayoutMap"
- "_keyLayoutMapReverse"
- "choseSecondary"
- "hasPrefix:"
- "initWithConfig:keyboardState:"
- "initializeKeyLayoutMaps"
- "internalStringToExternal:"
- "internalStringToExternal:ignoreCompositionDisabled:"
- "internalStringToSecondaryExternal:"
- "keyLayoutMap"
- "keyLayoutMapReverse"
- "length"
- "stringByAppendingString:"
- "substringWithRange:"
- "v16@0:8"
- "v8@?0"
- "validUSetForAutocorrectionSecondary"

```
