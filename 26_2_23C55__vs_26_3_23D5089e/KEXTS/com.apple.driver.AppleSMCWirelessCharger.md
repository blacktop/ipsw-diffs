## com.apple.driver.AppleSMCWirelessCharger

> `com.apple.driver.AppleSMCWirelessCharger`

```diff

-118.40.3.0.0
+118.80.4.0.0
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x2ad6
-  __TEXT.__os_log: 0x4e2
-  __TEXT_EXEC.__text: 0x100a0
+  __TEXT.__cstring: 0x2acb
+  __TEXT.__os_log: 0x553
+  __TEXT_EXEC.__text: 0x10278
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68
-  __DATA.__bss: 0x6c
-  __DATA_CONST.__auth_got: 0x2a8
+  __DATA.__bss: 0x7c
+  __DATA_CONST.__auth_got: 0x2b0
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x8

   __DATA_CONST.__const: 0xee0
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: B3CFE13E-EEFD-3301-8825-A85DB3A40F9E
+  UUID: 3613BDE9-D75F-3EC8-B141-1F0AF90D394A
   Functions: 180
   Symbols:   0
-  CStrings:  385
+  CStrings:  388
 
Functions:
~ sub_fffffe0009ba77e8 -> sub_fffffe0009c7cd88 : 5460 -> 5440
~ sub_fffffe0009bab4e0 -> sub_fffffe0009c80a6c : 136 -> 532
~ sub_fffffe0009bb46d0 -> sub_fffffe0009c89de8 : 872 -> 968
CStrings:
+ "%s dlog_addr: %08x, words_to_read: %d, active_buf_words: %d"
+ "%s: DLOG throttle disabled"
+ "%s: DLOG throttle enabled"
+ "peripheralLogWorkHandler"
- "%s::%s:Failed to read wrapped logs\n"

```
