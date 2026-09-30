## com.apple.security.AKSAnalytics

> `com.apple.security.AKSAnalytics`

```diff

-2155.0.18.502.1
+2155.0.23.502.1
   __TEXT.__const: 0x84
-  __TEXT.__cstring: 0x8f93
-  __TEXT.__os_log: 0x12d0
-  __TEXT_EXEC.__text: 0x4ae4
+  __TEXT.__cstring: 0x8fd6
+  __TEXT.__os_log: 0x12d4
+  __TEXT_EXEC.__text: 0x4b04
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x36a8
   __DATA.__common: 0x58

   __DATA_CONST.__got: 0x60
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x6e20
+  __DATA_CONST.__const: 0x6e40
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0xa0
-  UUID: BFD3A597-5451-3A12-99AD-46B80184028B
+  UUID: 74B60374-8744-3004-AFE0-F3299C543441
   Functions: 119
   Symbols:   0
-  CStrings:  1606
+  CStrings:  1608
 
Functions:
~ sub_fffffff008b3ed1c -> sub_fffffff008b4ee6c : 12 -> 20
~ sub_fffffff008b3ed28 -> sub_fffffff008b4ee80 : 20 -> 12
~ sub_fffffff008b3f0a8 -> sub_fffffff008b4f1f8 : 280 -> 288
~ sub_fffffff008b40160 -> sub_fffffff008b502b8 : 524 -> 548
CStrings:
+ "%s: checking (keybaghandle = %x) for unlock status\n"
+ "22:24:43"
+ "Jun 30 2025"
+ "erm"
+ "void AKSAnalytics::lockStateThreadCallHandler(keybag_handle_t)"
- "21:23:29"
- "Jun 17 2025"
- "checking (keybaghandle = %x) for unlock status\n"

```
