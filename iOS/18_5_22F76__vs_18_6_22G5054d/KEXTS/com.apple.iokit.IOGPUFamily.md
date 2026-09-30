## com.apple.iokit.IOGPUFamily

> `com.apple.iokit.IOGPUFamily`

```diff

-104.5.0.0.0
-  __TEXT.__cstring: 0x50af
+104.6.1.0.0
+  __TEXT.__cstring: 0x508f
   __TEXT.__os_log: 0x3984
   __TEXT.__const: 0x7c
-  __TEXT_EXEC.__text: 0x39088
+  __TEXT_EXEC.__text: 0x39028
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x4b0
-  __DATA.__common: 0x780
+  __DATA.__data: 0x410
+  __DATA.__common: 0x778
   __DATA.__bss: 0x9
   __DATA_CONST.__auth_got: 0x640
   __DATA_CONST.__got: 0xc8

   __DATA_CONST.__kalloc_type: 0x1000
   __DATA_CONST.__kalloc_var: 0xf00
   __DATA_CONST.__assert: 0x78
-  UUID: E9349498-E22C-3603-9BA4-A97CEA8032A3
+  UUID: 39D36A1C-1880-34E9-84AE-60916F6F4E0F
   Functions: 1736
   Symbols:   0
-  CStrings:  743
+  CStrings:  741
 
Functions:
~ __ZN11IOGPUDevice12new_resourceEP20IOGPUNewResourceArgsP26IOGPUNewResourceReturnDatayPj : 2584 -> 2512
~ sub_fffffff00a188d30 -> sub_fffffff00a22b538 : 304 -> 280
CStrings:
+ "%s: PID %d may be leaking IOGPUResource (count=%d)\n"
- "%s: PID %d likely leaking IOGPUResource (count=%d)\n"
- "Resource Limit Count"
- "rsrc_limit"

```
