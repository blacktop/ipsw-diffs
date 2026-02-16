## Diagnostic-3738

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-3738.appex/Diagnostic-3738`

```diff

-1066.80.3.0.0
-  __TEXT.__text: 0xab4
-  __TEXT.__auth_stubs: 0x1c0
+1066.100.26.0.0
+  __TEXT.__text: 0xbb4
+  __TEXT.__auth_stubs: 0x190
   __TEXT.__objc_stubs: 0x3e0
   __TEXT.__objc_methlist: 0xe8
   __TEXT.__cstring: 0x9c

   __TEXT.__objc_methtype: 0x6f
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0xa8
-  __DATA_CONST.__auth_got: 0xf0
+  __TEXT.__unwind_info: 0xb8
+  __DATA_CONST.__auth_got: 0xd8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__cfstring: 0x180

   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0982E092-8D96-31CE-A67D-39018EF7BCE5
+  UUID: 5DF9F9AA-1824-3EB2-BFEC-6ED1D71F5297
   Functions: 22
-  Symbols:   57
+  Symbols:   54
   CStrings:  90
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x24
Functions:
~ sub_100000d28 : 268 -> 264
~ sub_100000e34 -> sub_100000e30 : 412 -> 452
~ sub_100000fd8 -> sub_100000ffc : 12 -> 64
~ sub_100000fec -> sub_100001044 : 12 -> 64
~ sub_1000010d8 -> sub_100001164 : 808 -> 856
~ sub_100001418 -> sub_1000014d4 : 448 -> 480
~ _stringOrNull : 92 -> 100
~ _numberOrNull : 92 -> 100
~ sub_100001690 -> sub_10000177c : 136 -> 148
~ sub_100001758 -> sub_100001850 : 132 -> 140

```
