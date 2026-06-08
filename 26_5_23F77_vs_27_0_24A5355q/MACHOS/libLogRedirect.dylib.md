## libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

```diff

-64575.39.1.0.0
-  __TEXT.__text: 0x2078
-  __TEXT.__auth_stubs: 0x270
+64578.47.1.0.0
+  __TEXT.__text: 0x24b8
+  __TEXT.__auth_stubs: 0x290
   __TEXT.__init_offsets: 0x4
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x46c
+  __TEXT.__cstring: 0x4b9
   __TEXT.__oslogstring: 0x19
-  __TEXT.__unwind_info: 0xb0
-  __DATA_CONST.__auth_got: 0x138
+  __TEXT.__unwind_info: 0xc8
+  __DATA_CONST.__const: 0x60
+  __DATA_CONST.__auth_got: 0x148
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x48
   __AUTH_CONST.__interpose: 0x50
   __DATA.__data: 0x58
   __DATA.__common: 0x18
-  __DATA.__bss: 0x217c
+  __DATA.__bss: 0x21ac
   - /usr/lib/libSystem.B.dylib
-  UUID: 0D913EFF-8893-3040-9C4E-0F8D746C2F3E
-  Functions: 20
-  Symbols:   106
-  CStrings:  61
+  UUID: 50EFF61D-7B9E-3C14-A97F-BE34F4C0D668
+  Functions: 25
+  Symbols:   114
+  CStrings:  65
 
Symbols:
+ GetIsSystemFramework.SysPaths
+ _GetIsSystemFramework
+ _LogPredicate_Evaluate
+ _LogPredicate_Init
+ _LogPredicate_InitContext
+ _ParsePathList
+ _globalConfig
+ _malloc_type_malloc
+ _strsep
- HookIsSystemFramework.SysPaths
CStrings:
+ ":"
+ "OS_LOG_DT_ALLOW_PATHS"
+ "OS_LOG_DT_DENY_PATHS"
+ "com.apple.Previews.StubExecutor"

```
