## PhoneNumberResolver

> `/System/Library/PrivateFrameworks/PhoneNumberResolver.framework/PhoneNumberResolver`

```diff

   __TEXT.__gcc_except_tab: 0x198
   __TEXT.__cstring: 0x396
   __TEXT.__oslogstring: 0x820
-  __TEXT.__unwind_info: 0x1b8
+  __TEXT.__unwind_info: 0x1c0
   __TEXT.__objc_classname: 0xa1
   __TEXT.__objc_methname: 0xed4
   __TEXT.__objc_methtype: 0x222

   - /System/Library/PrivateFrameworks/PhoneNumbers.framework/PhoneNumbers
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9E35C6B5-05CF-3B7E-B329-799D88336854
+  UUID: D953EB0B-C2B6-3690-807E-A1C3E7FA8B4A
   Functions: 109
   Symbols:   564
   CStrings:  392
Functions:
~ +[PNRResourceManager sharedManager].cold.1 -> -[PNRPhoneNumberResolver init] : 20 -> 152
~ ___35+[PNRResourceManager sharedManager]_block_invoke -> -[PNRPhoneNumberResolver init].cold.1 : 60 -> 40
~ +[PNRResourceManager sharedManager] -> +[PNRResourceManager sharedManager].cold.1 : 68 -> 20
~ -[PNRPhoneNumberResolver init].cold.1 -> +[PNRResourceManager sharedManager] : 40 -> 68
~ -[PNRPhoneNumberResolver init] -> ___35+[PNRResourceManager sharedManager]_block_invoke : 152 -> 60

```
