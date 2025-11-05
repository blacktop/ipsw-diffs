## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/Resources/DesktopServicesHelper`

```diff

-1732.3.4.0.0
-  __TEXT.__text: 0x62594
-  __TEXT.__auth_stubs: 0x1b40
+1732.4.6.0.0
+  __TEXT.__text: 0x6014c
+  __TEXT.__auth_stubs: 0x1b80
   __TEXT.__objc_stubs: 0x1700
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x534
-  __TEXT.__const: 0x1230
-  __TEXT.__gcc_except_tab: 0x84ec
-  __TEXT.__objc_methname: 0x15bb
+  __TEXT.__objc_methlist: 0x564
+  __TEXT.__gcc_except_tab: 0x85c8
+  __TEXT.__const: 0x1220
+  __TEXT.__objc_methname: 0x15ca
   __TEXT.__objc_classname: 0xc5
-  __TEXT.__objc_methtype: 0xb4c
-  __TEXT.__cstring: 0x1dae
-  __TEXT.__oslogstring: 0x10ff
+  __TEXT.__objc_methtype: 0xb51
+  __TEXT.__cstring: 0x1daa
+  __TEXT.__oslogstring: 0x13d0
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2b40
-  __DATA_CONST.__auth_got: 0xdb8
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1110
+  __TEXT.__unwind_info: 0x2b08
+  __DATA_CONST.__auth_got: 0xdd8
+  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__const: 0x1128
   __DATA_CONST.__cfstring: 0xe20
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_intobj: 0xa8
-  __DATA.__objc_const: 0x9a8
-  __DATA.__objc_selrefs: 0x6a0
+  __DATA_CONST.__objc_intobj: 0x48
+  __DATA.__objc_const: 0x968
+  __DATA.__objc_selrefs: 0x6b0
   __DATA.__objc_ivar: 0x58
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x159
-  __DATA.__bss: 0x9d8
+  __DATA.__bss: 0x9f8
   __DATA.__common: 0x1d2
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E63FA7B6-83CD-38E3-8B0B-3DC753A9D04C
-  Functions: 1545
-  Symbols:   617
-  CStrings:  906
+  UUID: 141DB79F-59C7-36DC-9D3A-251FD822467D
+  Functions: 1519
+  Symbols:   624
+  CStrings:  918
 
Symbols:
+ __ZNSt19bad_optional_accessD1Ev
+ __ZNSt3__117bad_function_callD1Ev
+ __ZTINSt3__117bad_function_callE
+ __ZTISt19bad_optional_access
+ __ZTVNSt3__117bad_function_callE
+ __ZTVSt19bad_optional_access
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _fchmodat
+ _lchmod
- _CFURLIsFileReferenceURL
- __ZNKSt9exception4whatEv
- __ZNSt9exceptionD2Ev
- __ZTISt9exception
- ___kCFBooleanFalse
CStrings:
+ "%{public}@ is owned by %d already."
+ "%{public}@ is owned by %d repairing owner to %d"
+ "B32@0:8r^v16^B24"
+ "Error removing checkpoint '%d' for %{public}@"
+ "Failed to revert acls on %{public}@ error=%d"
+ "Failed to revert mode on %{public}@ error=%d"
+ "Failed to revert uid to %d on %{public}@ error=%d"
+ "Failed with error(%d) to repair owner to %d for %{public}@"
+ "No Audit token found in message from Scripting"
+ "Set acl on %{public}@ succeeded"
+ "Set acl on '%{public}@' failed with error=%d"
+ "Set permissions failed with error=%d"
+ "Sizer found dataless item %{public}@ on local volume - marking as conflict"
+ "Sizer found dataless item %{public}@ on non-local volume - skipping conflict"
+ "Skipping resumable copy for uchg setting on %{public}@"
+ "Unable to find directory %{public}@ error=%d"
+ "null value for acl, attempting to use an empty acl instead"
+ "writeToTarget:useCheckpoints:"
- "B24@0:8^v16"
- "I"
- "Set acl on '%{public}@' with status=%d"
- "Set permissions failed rolling back acl"
- "writeToTarget:"

```
