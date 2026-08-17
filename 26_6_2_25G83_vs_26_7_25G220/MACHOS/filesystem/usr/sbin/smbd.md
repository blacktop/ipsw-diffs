## smbd

> `usr/sbin/smbd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__const`
- `__TEXT.__dof_ntvfs`
- `__TEXT.__dof_smbd`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__data`

```diff

-666.100.1.0.0
-  __TEXT.__text: 0x7c494
+666.100.1.700.1
+  __TEXT.__text: 0x7c6c8
   __TEXT.__auth_stubs: 0x1f80
   __TEXT.__init_offsets: 0x14
   __TEXT.__const: 0x1267
-  __TEXT.__gcc_except_tab: 0x5a0c
-  __TEXT.__oslogstring: 0x9f1f
-  __TEXT.__cstring: 0xff52
+  __TEXT.__gcc_except_tab: 0x5a18
+  __TEXT.__oslogstring: 0xa019
+  __TEXT.__cstring: 0xff67
   __TEXT.__dof_ntvfs: 0x1eed
   __TEXT.__dof_smbd: 0x7aa
   __TEXT.__unwind_info: 0x2110

   - /usr/lib/libpam.2.dylib
   Functions: 1622
   Symbols:   2734
-  CStrings:  3190
+  CStrings:  3196
 
Symbols:
+ __ZL19reply_buffer_appendIN4smb214ioctl_responseEEbR11smb_requestRKT_
- _Z19smb2_dispatch_ioctlR11smb_requestPhS1_
Functions:
~ __Z19smb2_dispatch_ioctlR11smb_requestPhS1_ : 3492 -> 3504
~ __ZL11copy_chunksR11smb_requestN8platform11counted_ptrIN5ntvfs11file_handleEEEPhS6_RNS3_15file_operations13fsctl_resultsE : 1532 -> 2108
~ _Z19smb2_dispatch_ioctlR11smb_requestPhS1_.cold.1 -> __ZL19reply_buffer_appendIN4smb214ioctl_responseEEbR11smb_requestRKT_ : 196 -> 172
CStrings:
+ "%s: Chunk Count: %u exceeds server maximum: %u"
+ "%s: FSCTL_SRV_COPY_CHUNK MaxOutputResponse: %u too small"
+ "%s: chunk: %u length: %u exceeds server maximum: %u"
+ "%s: chunk: %u total data size: %llu exceeds server maximum: %u"
+ "%s: failed to extract chunk %u"
+ "preflight_copychunks"
```
