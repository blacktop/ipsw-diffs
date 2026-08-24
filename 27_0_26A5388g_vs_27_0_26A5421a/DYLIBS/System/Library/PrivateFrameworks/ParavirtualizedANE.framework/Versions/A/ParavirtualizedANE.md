## ParavirtualizedANE

> `/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/Versions/A/ParavirtualizedANE`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-382.12.0.0.0
-  __TEXT.__text: 0x21a10
-  __TEXT.__objc_methlist: 0x7e4
+382.15.1.0.0
+  __TEXT.__text: 0x22204
+  __TEXT.__objc_methlist: 0x814
   __TEXT.__const: 0x188
   __TEXT.__cstring: 0xf6e
-  __TEXT.__oslogstring: 0x6475
-  __TEXT.__gcc_except_tab: 0x3bcc
-  __TEXT.__unwind_info: 0x738
+  __TEXT.__oslogstring: 0x65cf
+  __TEXT.__gcc_except_tab: 0x3d1c
+  __TEXT.__unwind_info: 0x750
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0x20
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa28
+  __DATA_CONST.__objc_selrefs: 0xa58
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__got: 0x1b0
+  __DATA_CONST.__got: 0x1c0
   __AUTH_CONST.__const: 0x130
   __AUTH_CONST.__cfstring: 0x11c0
-  __AUTH_CONST.__objc_const: 0x540
+  __AUTH_CONST.__objc_const: 0x570
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x258
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x48
+  __DATA.__objc_ivar: 0x4c
   __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 543
-  Symbols:   848
-  CStrings:  558
+  Functions: 549
+  Symbols:   863
+  CStrings:  562
 
Symbols:
+ -[_ANEVirtualModel baseKeeperProgram]
+ -[_ANEVirtualModel setBaseKeeperProgram:]
+ -[_ANEVirtualPlatformClient ensureBaseKeeperClientForBaseModelIdentifier:]
+ -[_ANEVirtualPlatformClient teardownFailedInstanceForVirtualModel:programHandle:]
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table129
+ GCC_except_table130
+ GCC_except_table146
+ GCC_except_table147
+ GCC_except_table155
+ GCC_except_table156
+ GCC_except_table161
+ GCC_except_table162
+ GCC_except_table46
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table66
+ GCC_except_table69
+ GCC_except_table72
+ GCC_except_table73
+ GCC_except_table77
+ GCC_except_table82
+ GCC_except_table92
+ GCC_except_table98
+ OBJC_IVAR_$__ANEVirtualModel._baseKeeperProgram
+ _OBJC_CLASS_$__ANEProgramForEvaluation
+ _objc_msgSend$allValues
+ _objc_msgSend$baseKeeperProgram
+ _objc_msgSend$ensureBaseKeeperClientForBaseModelIdentifier:
+ _objc_msgSend$programWithHandle:intermediateBufferHandle:queueDepth:
+ _objc_msgSend$setBaseKeeperProgram:
+ _objc_msgSend$teardownFailedInstanceForVirtualModel:programHandle:
+ _vm_kernel_page_size
- GCC_except_table100
- GCC_except_table108
- GCC_except_table109
- GCC_except_table114
- GCC_except_table115
- GCC_except_table143
- GCC_except_table144
- GCC_except_table150
- GCC_except_table153
- GCC_except_table158
- GCC_except_table159
- GCC_except_table48
- GCC_except_table61
- GCC_except_table62
- GCC_except_table68
- GCC_except_table71
- GCC_except_table74
- GCC_except_table75
- GCC_except_table79
- GCC_except_table84
- GCC_except_table94
CStrings:
+ "%@: ERROR IOSurface size (%llu) not within page padding of IOBuffer size (%llu) for procedure=%@, error=%@!"
+ "%@: base model for identifier=%@ not found in cache; cannot keep base direct-path client alive"
+ "%@: failed to open persistent base direct-path client for base programHandle=%llu"
+ "%@: failed to unload orphaned instance for programHandle=%llu, error=%@"
+ "%@: keeping base direct-path client alive for base programHandle=%llu identifier=%@"
- "%@: ERROR IOSurface size (%llu) doesn't match IOBuffer size (%llu) for procedure=%@, error=%@!"
```
