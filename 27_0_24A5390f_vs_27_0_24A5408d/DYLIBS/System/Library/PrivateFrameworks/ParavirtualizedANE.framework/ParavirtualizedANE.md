## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-382.12.0.0.0
-  __TEXT.__text: 0x1fb48
-  __TEXT.__objc_methlist: 0x7e4
+382.15.1.0.0
+  __TEXT.__text: 0x202a4
+  __TEXT.__objc_methlist: 0x814
   __TEXT.__const: 0x190
   __TEXT.__cstring: 0xf6e
-  __TEXT.__oslogstring: 0x64a6
-  __TEXT.__gcc_except_tab: 0x3b48
-  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__oslogstring: 0x6600
+  __TEXT.__gcc_except_tab: 0x3c98
+  __TEXT.__unwind_info: 0x708
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x70
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa18
+  __DATA_CONST.__objc_selrefs: 0xa48
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__got: 0x1b8
   __AUTH_CONST.__const: 0xd0
   __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0x540
+  __AUTH_CONST.__objc_const: 0x570
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__auth_got: 0x328
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x48
+  __DATA.__objc_ivar: 0x4c
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 539
-  Symbols:   855
-  CStrings:  559
+  Functions: 545
+  Symbols:   871
+  CStrings:  563
 
Symbols:
+ -[_ANEVirtualModel baseKeeperProgram]
+ -[_ANEVirtualModel setBaseKeeperProgram:]
+ -[_ANEVirtualPlatformClient ensureBaseKeeperClientForBaseModelIdentifier:]
+ -[_ANEVirtualPlatformClient teardownFailedInstanceForVirtualModel:programHandle:]
+ GCC_except_table104
+ GCC_except_table105
+ GCC_except_table110
+ GCC_except_table111
+ GCC_except_table126
+ GCC_except_table127
+ GCC_except_table143
+ GCC_except_table151
+ GCC_except_table152
+ GCC_except_table156
+ GCC_except_table44
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table64
+ GCC_except_table67
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table75
+ GCC_except_table80
+ GCC_except_table90
+ GCC_except_table96
+ _OBJC_CLASS_$__ANEProgramForEvaluation
+ _OBJC_IVAR_$__ANEVirtualModel._baseKeeperProgram
+ _objc_msgSend$allValues
+ _objc_msgSend$baseKeeperProgram
+ _objc_msgSend$ensureBaseKeeperClientForBaseModelIdentifier:
+ _objc_msgSend$programWithHandle:intermediateBufferHandle:queueDepth:
+ _objc_msgSend$setBaseKeeperProgram:
+ _objc_msgSend$teardownFailedInstanceForVirtualModel:programHandle:
+ _objc_retain_x24
+ _vm_kernel_page_size
- GCC_except_table106
- GCC_except_table107
- GCC_except_table112
- GCC_except_table113
- GCC_except_table141
- GCC_except_table148
- GCC_except_table149
- GCC_except_table154
- GCC_except_table46
- GCC_except_table59
- GCC_except_table60
- GCC_except_table66
- GCC_except_table69
- GCC_except_table72
- GCC_except_table73
- GCC_except_table77
- GCC_except_table82
- GCC_except_table92
- GCC_except_table98
CStrings:
+ "%@: ERROR IOSurface size (%llu) not within page padding of IOBuffer size (%llu) for procedure=%@, error=%@!"
+ "%@: base model for identifier=%@ not found in cache; cannot keep base direct-path client alive"
+ "%@: failed to open persistent base direct-path client for base programHandle=%llu"
+ "%@: failed to unload orphaned instance for programHandle=%llu, error=%@"
+ "%@: keeping base direct-path client alive for base programHandle=%llu identifier=%@"
- "%@: ERROR IOSurface size (%llu) doesn't match IOBuffer size (%llu) for procedure=%@, error=%@!"
```
