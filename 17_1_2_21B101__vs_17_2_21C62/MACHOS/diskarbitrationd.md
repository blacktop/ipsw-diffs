## diskarbitrationd

> `/usr/libexec/diskarbitrationd`

```diff

-435.0.0.0.0
-  __TEXT.__text: 0x15b50
-  __TEXT.__auth_stubs: 0x1470
-  __TEXT.__objc_stubs: 0x660
+438.0.0.0.0
+  __TEXT.__text: 0x157c0
+  __TEXT.__auth_stubs: 0x1460
+  __TEXT.__objc_stubs: 0x500
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__cstring: 0x2819
+  __TEXT.__cstring: 0x2711
   __TEXT.__const: 0x68
   __TEXT.__gcc_except_tab: 0x58
-  __TEXT.__objc_methname: 0x50a
+  __TEXT.__objc_methname: 0x42c
   __TEXT.__oslogstring: 0xfc
   __TEXT.__objc_classname: 0x31
   __TEXT.__objc_methtype: 0x10f
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x4ec
-  __DATA_CONST.__auth_got: 0xa48
-  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__auth_got: 0xa40
+  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0xaa0
-  __DATA_CONST.__cfstring: 0x1980
+  __DATA_CONST.__cfstring: 0x1900
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x240
-  __DATA.__objc_selrefs: 0x1f0
-  __DATA.__objc_classrefs: 0x70
+  __DATA.__objc_selrefs: 0x198
+  __DATA.__objc_classrefs: 0x60
   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD6A2DD6-8B20-36C8-9C25-111636CF6934
+  UUID: 608F0759-530D-30E3-93DB-642B983CD668
   Functions: 455
-  Symbols:   373
-  CStrings:  788
+  Symbols:   369
+  CStrings:  763
 
Symbols:
+ _OBJC_CLASS_$_FSKitDiskArbHelper
- _NSPOSIXErrorDomain
- _OBJC_CLASS_$_LiveFSMountClient
- _OBJC_CLASS_$_LiveFSUSBLocalStorageClient
- _OBJC_CLASS_$_NSError
- _objc_enumerationMutation
CStrings:
+ "Attempt to use FSKit, when not present, to mount volume of type %@"
+ "DAMountUserFSVolume:deviceName:mountPoint:volumeName:mountOptions:"
- "%@ loadVolumes failed with %@"
- "%@ mount failed with %@"
- "%@ mounting with name %@, error %@, and how 0x%x."
- "%@: got 2 different names from probe and userfs: p->%@  u->%@"
- "Mounted %@ successfully."
- "com.apple.filesystems.UserFS.FileProvider"
- "countByEnumeratingWithState:objects:count:"
- "errorForDomain"
- "errorWithDomain:code:userInfo:"
- "forgetVolume:withFlags:"
- "how"
- "intValue"
- "integerValue"
- "isEqual:"
- "loadVolumes:ofType:withError:"
- "mountVolume:displayName:provider:domainError:on:how:"
- "newClientForProvider:"
- "newManager"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "unload for volume %@ failed with %@"
- "unsupported error code for domain: %d"

```
