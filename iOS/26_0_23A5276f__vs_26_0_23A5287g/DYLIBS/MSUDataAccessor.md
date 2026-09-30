## MSUDataAccessor

> `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor`

```diff

   __TEXT.__gcc_except_tab: 0x210
   __TEXT.__cstring: 0x9f1
   __TEXT.__oslogstring: 0x1e3
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__unwind_info: 0x140
   __TEXT.__objc_classname: 0x68
   __TEXT.__objc_methname: 0x66a
   __TEXT.__objc_methtype: 0xd8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpartition2_dynamic.dylib
-  UUID: 2B0E8FD0-9FD0-301C-92B1-29A92C2ED5A1
+  UUID: 67C0D846-7B67-38B6-ADA4-F1E1FB36CEC8
   Functions: 64
   Symbols:   313
   CStrings:  324
Functions:
~ _OUTLINED_FUNCTION_0 -> _MSUDASharedLogger : 12 -> 68
~ _OUTLINED_FUNCTION_0 -> -[MSUDataAccessorSymbolicPathResolver dealloc] : 28 -> 80
~ +[MSUDataAccessor sharedDataAccessor] -> -[MSUDataAccessorSymbolicPathResolver .cxx_destruct] : 68 -> 12
~ ___37+[MSUDataAccessor sharedDataAccessor]_block_invoke -> +[MSUDataAccessor sharedDataAccessor] : 148 -> 68
~ -[MSUDataAccessor init] -> ___37+[MSUDataAccessor sharedDataAccessor]_block_invoke : 56 -> 148
~ _MSUDASharedLogger -> -[MSUDataAccessor init] : 68 -> 56
~ -[MSUDataAccessorDiagnostics returnDirectoryIfExistsForPath:] -> _OUTLINED_FUNCTION_0 : 172 -> 12
~ -[MSUDataAccessorDiagnostics specialCaseFDRPathForDiagnostics] -> -[MSUDataAccessorDiagnostics returnDirectoryIfExistsForPath:] : 12 -> 172
~ -[MSUDataAccessorDiagnostics copyPathForPersistentData:error:] -> -[MSUDataAccessorDiagnostics specialCaseFDRPathForDiagnostics] : 120 -> 12
~ +[MSUDataAccessorSymbolicPathResolver symbolicPathResolver] -> -[MSUDataAccessorDiagnostics copyPathForPersistentData:error:] : 48 -> 120
~ +[MSUDataAccessorSymbolicPathResolver resolvedSymbol:error:] -> +[MSUDataAccessorSymbolicPathResolver symbolicPathResolver] : 2052 -> 48
~ ___60+[MSUDataAccessorSymbolicPathResolver resolvedSymbol:error:]_block_invoke -> +[MSUDataAccessorSymbolicPathResolver resolvedSymbol:error:] : 64 -> 2052
~ -[MSUDataAccessorSymbolicPathResolver init] -> ___60+[MSUDataAccessorSymbolicPathResolver resolvedSymbol:error:]_block_invoke : 104 -> 64
~ -[MSUDataAccessorSymbolicPathResolver dealloc] -> -[MSUDataAccessorSymbolicPathResolver init] : 80 -> 104
~ -[MSUDataAccessorSymbolicPathResolver .cxx_destruct] -> _OUTLINED_FUNCTION_0 : 12 -> 28

```
