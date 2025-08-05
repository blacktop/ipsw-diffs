## com.apple.iokit.IOThunderboltFamily

> `com.apple.iokit.IOThunderboltFamily`

```diff

-6800.0.1.0.0
-  __TEXT.__cstring: 0x36578
+6800.0.2.0.1
+  __TEXT.__cstring: 0x365c9
   __TEXT.__os_log: 0x2f2f3
   __TEXT.__const: 0xac8
-  __TEXT_EXEC.__text: 0x19feb4
+  __TEXT_EXEC.__text: 0x19ffc0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xb1a
   __DATA.__common: 0x1378

   __DATA_CONST.__const: 0x1f930
   __DATA_CONST.__kalloc_type: 0x1f40
   __DATA_CONST.__kalloc_var: 0xbe0
-  UUID: 0CFCCC7B-70EF-3761-8EA0-4549BF912CAB
+  UUID: 151AD984-FDD5-3C7A-90EA-1175CF49DD7E
   Functions: 4967
   Symbols:   0
-  CStrings:  4979
+  CStrings:  4980
 
Functions:
~ sub_fffffff00a8e3fcc -> sub_fffffff00a8e55ec : 332 -> 348
~ __ZN17IOThunderboltPort15enableUniDirTMUEb : 1312 -> 1452
~ sub_fffffff00a9e187c -> sub_fffffff00a9e2f38 : 1256 -> 1252
~ __ZN38IOTBTTunnelDriverClientDrivenInterface17waitForClientStopEj : 1928 -> 2044
CStrings:
+ "%lldus IOThunderboltSwitch(%x@%llx)::configureCLx - enable CL1/2 value = 0x%08x\n"
+ "21:46:20"
+ "Jul 25 2025"
- "21:46:45"
- "Jul 15 2025"

```
