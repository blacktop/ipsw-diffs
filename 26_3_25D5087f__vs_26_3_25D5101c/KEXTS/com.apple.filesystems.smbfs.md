## com.apple.filesystems.smbfs

> `com.apple.filesystems.smbfs`

```diff

-532.80.2.0.0
+532.80.3.0.0
   __TEXT.__const: 0xbe5
   __TEXT.__cstring: 0x489d
   __TEXT.__os_log: 0x15e62
-  __TEXT_EXEC.__text: 0x7e510
+  __TEXT_EXEC.__text: 0x7e550
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xdf8
   __DATA.__bss: 0x106c

   __DATA_CONST.__const: 0x78
   __DATA_CONST.__kalloc_type: 0x4d80
   __DATA_CONST.__kalloc_var: 0x460
-  UUID: D0A77B7B-4D54-39B5-92E4-C366845D274E
+  UUID: 3D656905-7A30-341C-832B-E9635025B4F7
   Functions: 763
   Symbols:   3734
   CStrings:  2496
Symbols:
+ smb_iod_create.kalloc_type_view_4225
+ smb_iod_create.kalloc_type_view_4243
+ smb_iod_create.kalloc_type_view_4271
+ smb_iod_destroy.kalloc_type_view_4341
+ smb_iod_destroy.kalloc_type_view_4345
+ smb_iod_destroy.kalloc_type_view_4372
+ smb_iod_lease_dequeue.kalloc_type_view_4824
+ smb_iod_lease_enqueue.kalloc_type_view_4121
+ smb_iod_main.kalloc_type_view_3924
+ smb_iod_request.kalloc_type_view_2281
+ smb_iod_request.kalloc_type_view_2337
+ smb_iod_thread.kalloc_type_view_4027
- smb_iod_create.kalloc_type_view_4218
- smb_iod_create.kalloc_type_view_4236
- smb_iod_create.kalloc_type_view_4264
- smb_iod_destroy.kalloc_type_view_4334
- smb_iod_destroy.kalloc_type_view_4338
- smb_iod_destroy.kalloc_type_view_4365
- smb_iod_lease_dequeue.kalloc_type_view_4817
- smb_iod_lease_enqueue.kalloc_type_view_4114
- smb_iod_main.kalloc_type_view_3917
- smb_iod_request.kalloc_type_view_2274
- smb_iod_request.kalloc_type_view_2330
- smb_iod_thread.kalloc_type_view_4020
Functions:
~ _smb_iod_sendrq : 1392 -> 1424
~ _smb_iod_read_thread : 3296 -> 3328

```
