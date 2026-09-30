## CarKit

> `/System/Library/PrivateFrameworks/CarKit.framework/CarKit`

```diff

-  __TEXT.__text: 0x613c8
+  __TEXT.__text: 0x619d0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x62b4
-  __TEXT.__const: 0x548
-  __TEXT.__gcc_except_tab: 0x984
-  __TEXT.__oslogstring: 0x6aa6
-  __TEXT.__cstring: 0x5a8d
+  __TEXT.__objc_methlist: 0x62fc
+  __TEXT.__const: 0x558
+  __TEXT.__gcc_except_tab: 0x9e8
+  __TEXT.__oslogstring: 0x6ae6
+  __TEXT.__cstring: 0x5a9d
   __TEXT.__dlopen_cstrs: 0x15e
   __TEXT.__constg_swiftt: 0x1a0
-  __TEXT.__swift5_typeref: 0x17c
+  __TEXT.__swift5_typeref: 0x188
   __TEXT.__swift5_fieldmd: 0x94
   __TEXT.__swift5_types: 0x1c
   __TEXT.__swift5_reflstr: 0x88
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__unwind_info: 0x1bd8
+  __TEXT.__unwind_info: 0x1bd0
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36c0
+  __DATA_CONST.__objc_selrefs: 0x36e0
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0xc0
   __DATA_CONST.__got: 0x870
   __AUTH_CONST.__const: 0x1bb0
   __AUTH_CONST.__cfstring: 0x5c40
-  __AUTH_CONST.__objc_const: 0x10230
+  __AUTH_CONST.__objc_const: 0x10290
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0xac8
   __AUTH.__objc_data: 0x1400
-  __AUTH.__data: 0x1b0
-  __DATA.__objc_ivar: 0x724
-  __DATA.__data: 0x1194
+  __AUTH.__data: 0x1b8
+  __DATA.__objc_ivar: 0x72c
+  __DATA.__data: 0x11a0
   __DATA.__bss: 0x740
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0xc8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3032
-  Symbols:   9613
-  CStrings:  2154
+  Functions: 3038
+  Symbols:   9630
+  CStrings:  2155
 
Sections:
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[CARSession initWithFigEndpoint:sessionStatusOptions:nightModeProvider:]
+ -[CARSession nightModeProvider]
+ -[CARSession setNightModeProvider:]
+ -[CARSessionStatus initForCarPlayShellWithNightModeProvider:]
+ -[CARSessionStatus initWithOptions:nightModeProvider:]
+ -[CARSessionStatus nightModeProvider]
+ -[CARSessionStatus setNightModeProvider:]
+ GCC_except_table155
+ GCC_except_table179
+ GCC_except_table185
+ GCC_except_table213
+ _AFIsLinwoodEnabledAndWasEverAvailable
+ _AFIsLinwoodEnabledAndWasEverAvailable$delayInitStub
+ _OBJC_IVAR_$_CARSession._nightModeProvider
+ _OBJC_IVAR_$_CARSessionStatus._nightModeProvider
+ ___54-[CARSessionStatus initWithOptions:nightModeProvider:]_block_invoke
+ ___54-[CARSessionStatus initWithOptions:nightModeProvider:]_block_invoke_2
+ ___73-[CARSession initWithFigEndpoint:sessionStatusOptions:nightModeProvider:]_block_invoke
+ ___73-[CARSession initWithFigEndpoint:sessionStatusOptions:nightModeProvider:]_block_invoke_2
+ _objc_msgSend$initWithFigEndpoint:sessionStatusOptions:nightModeProvider:
+ _objc_msgSend$initWithOptions:nightModeProvider:
+ _objc_msgSend$initWithScreens:screenDisplayDictionaries:screenSupportsDDPContent:initialSystemNightMode:initialLocationBasedNightMode:defaultUserInterfaceStyle:ddpNightModeByScreen:
+ _objc_msgSend$nightModeProvider
+ _symbolic _____ySSSbG s18_DictionaryStorageC
- -[CARSession initWithFigEndpoint:sessionStatusOptions:]
- GCC_except_table152
- GCC_except_table175
- GCC_except_table181
- GCC_except_table207
- _AFIsLinwoodEnabledAndAvailable
- _AFIsLinwoodEnabledAndAvailable$delayInitStub
- ___36-[CARSessionStatus initWithOptions:]_block_invoke
- ___36-[CARSessionStatus initWithOptions:]_block_invoke_2
- ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke
- ___55-[CARSession initWithFigEndpoint:sessionStatusOptions:]_block_invoke_2
- _objc_msgSend$initWithFigEndpoint:sessionStatusOptions:
- _objc_msgSend$initWithScreens:screenDisplayDictionaries:screenSupportsDDPContent:initialSystemNightMode:initialLocationBasedNightMode:defaultUserInterfaceStyle:
CStrings:
+ "Linwood not enabled or was never available, hiding Campo from CarPlay"
+ "[DDPNightMode] screen %{public}@ nightMode=%d"
- "Linwood not enabled and available, hiding Campo from CarPlay"

```
