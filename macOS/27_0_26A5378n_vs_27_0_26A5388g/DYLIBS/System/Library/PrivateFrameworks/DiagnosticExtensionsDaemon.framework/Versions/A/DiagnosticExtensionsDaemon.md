## DiagnosticExtensionsDaemon

> `/System/Library/PrivateFrameworks/DiagnosticExtensionsDaemon.framework/Versions/A/DiagnosticExtensionsDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-220.0.0.0.0
-  __TEXT.__text: 0x7dca4
-  __TEXT.__objc_methlist: 0x6f54
+221.0.0.0.0
+  __TEXT.__text: 0x7db84
+  __TEXT.__objc_methlist: 0x6f7c
   __TEXT.__const: 0x372
-  __TEXT.__cstring: 0x5570
-  __TEXT.__gcc_except_tab: 0x1af0
-  __TEXT.__oslogstring: 0x9658
+  __TEXT.__cstring: 0x5530
+  __TEXT.__gcc_except_tab: 0x1ad0
+  __TEXT.__oslogstring: 0x9638
   __TEXT.__ustring: 0xc
   __TEXT.__constg_swiftt: 0x8c
   __TEXT.__swift5_typeref: 0x48

   __TEXT.__swift5_reflstr: 0x80
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1d98
+  __TEXT.__unwind_info: 0x1d90
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b58
+  __DATA_CONST.__objc_selrefs: 0x3b68
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1b0
   __DATA_CONST.__objc_arraydata: 0x48
-  __DATA_CONST.__got: 0x6d8
-  __AUTH_CONST.__const: 0x2270
-  __AUTH_CONST.__cfstring: 0x4e00
-  __AUTH_CONST.__objc_const: 0x139d8
+  __DATA_CONST.__got: 0x6c8
+  __AUTH_CONST.__const: 0x2240
+  __AUTH_CONST.__cfstring: 0x4de0
+  __AUTH_CONST.__objc_const: 0x13a08
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x548
   __AUTH.__objc_data: 0x90
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x5d8
+  __DATA.__objc_ivar: 0x5dc
   __DATA.__data: 0xad0
   __DATA.__bss: 0x1c0
   __DATA_DIRTY.__objc_data: 0x18e0

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreFollowUp.framework/Versions/A/CoreFollowUp
   - /System/Library/PrivateFrameworks/DiagnosticExtensions.framework/Versions/A/DiagnosticExtensions
+  - /System/Library/PrivateFrameworks/DiagnosticExtensionsKit.framework/Versions/A/DiagnosticExtensionsKit
   - /System/Library/PrivateFrameworks/EnhancedLogging.framework/Versions/A/EnhancedLogging
   - /System/Library/PrivateFrameworks/EnhancedLoggingState.framework/Versions/A/EnhancedLoggingState
   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2970
-  Symbols:   5931
-  CStrings:  1763
+  Functions: 2971
+  Symbols:   5929
+  CStrings:  1760
 
Symbols:
+ -[DEDDiagnosticCollector cachedExtensionManager]
+ -[DEDDiagnosticCollector deExtensionForIdentifier:]
+ -[DEDDiagnosticCollector setCachedExtensionManager:]
+ OBJC_IVAR_$_DEDDiagnosticCollector._cachedExtensionManager
+ _OBJC_CLASS_$_DEKExtensionManager
+ _objc_msgSend$deExtensionForIdentifier:
- GCC_except_table14
- _NSExtensionPointName
- _OBJC_CLASS_$_DEExtensionManager
- _OBJC_CLASS_$_NSExtension
- __56-[DEDDiagnosticCollector isDiagnosticExtensionAvailable]_block_invoke
- ___56-[DEDDiagnosticCollector isDiagnosticExtensionAvailable]_block_invoke
- ___block_descriptor_56_e8_32s40s48r_e29_v24?0"NSArray"8"NSError"16l
- _objc_msgSend$extensionsWithMatchingAttributes:completion:
CStrings:
- "Error finding diagnostic extension [%@]"
- "com.apple.diagnosticextensions-service"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
```
