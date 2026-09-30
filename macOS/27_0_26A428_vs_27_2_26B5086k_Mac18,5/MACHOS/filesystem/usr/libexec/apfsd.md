## apfsd

> `/usr/libexec/apfsd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_superrefs`
- `__DATA.__objc_data`

```diff

-3288.1.3.0.0
-  __TEXT.__text: 0x12dd4
-  __TEXT.__auth_stubs: 0xf70
+3288.40.13.0.0
+  __TEXT.__text: 0xeeb8
+  __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_stubs: 0x720
   __TEXT.__objc_methlist: 0x94
-  __TEXT.__cstring: 0x25c1
-  __TEXT.__const: 0x2e0
-  __TEXT.__oslogstring: 0x31be
-  __TEXT.__gcc_except_tab: 0x2f4
+  __TEXT.__cstring: 0x20a7
+  __TEXT.__const: 0x1f0
+  __TEXT.__oslogstring: 0x274b
   __TEXT.__objc_methname: 0x4c7
   __TEXT.__objc_classname: 0x12
   __TEXT.__objc_methtype: 0xb5
-  __TEXT.__unwind_info: 0x508
-  __DATA_CONST.__const: 0x410
-  __DATA_CONST.__cfstring: 0x2320
+  __TEXT.__unwind_info: 0x358
+  __DATA_CONST.__const: 0x1a0
+  __DATA_CONST.__cfstring: 0x22c0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x7c8
-  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_got: 0x6c8
+  __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__objc_const: 0x198
   __DATA.__objc_selrefs: 0x1d8

   __DATA.__objc_superrefs: 0x8
   __DATA.__objc_ivar: 0x20
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0xcc
-  __DATA.__common: 0x64
+  __DATA.__data: 0xc4
+  __DATA.__common: 0x5c
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/DiskArbitration.framework/Versions/A/DiskArbitration
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 248
-  Symbols:   325
-  CStrings:  792
+  Functions: 189
+  Symbols:   280
+  CStrings:  671
 
Symbols:
- _CFErrorCopyFailureReason
- _CFErrorGetCode
- _CFStringCreateWithFormat
- _CFStringGetIntValue
- _CFStringGetMaximumSizeForEncoding
- _ODNodeCreateWithNodeType
- _ODQueryCopyResults
- _ODQueryCreateWithNode
- _ODRecordCopyValues
- _ODSessionCreate
- __Unwind_Resume
- __ZNSt11logic_errorC2EPKc
- __ZNSt12length_errorD1Ev
- __ZNSt12out_of_rangeD1Ev
- __ZSt9terminatev
- __ZTISt12length_error
- __ZTISt12out_of_range
- __ZTVN10__cxxabiv117__class_type_infoE
- __ZTVN10__cxxabiv120__si_class_type_infoE
- __ZTVSt12length_error
- __ZTVSt12out_of_range
- __ZdaPv
- __ZdlPv
- __Znam
- __Znwm
- ___cxa_allocate_exception
- ___cxa_begin_catch
- ___cxa_end_catch
- ___cxa_free_exception
- ___cxa_pure_virtual
- ___cxa_throw
- ___gxx_personality_v0
- __os_log_default
- _fts_close
- _fts_open
- _fts_read
- _fts_set
- _kODAttributeTypeNFSHomeDirectory
- _kODAttributeTypeUniqueID
- _kODRecordTypeUsers
- _memcmp
- _printf
- _puts
- _strlen
- _sysctlbyname
CStrings:
+ "3288.40.13"
+ "D:dfh"
+ "IOMatchCategory"
+ "mount_apfs"
- "%s:%d: Cannot statfs /private/var\n"
- "%s:%u Err: Abort requested\n"
- "%s:%u Err: Dump failed, most likely we ran out of memory\n"
- "%s:%u Err: Failed to create OD Node\n"
- "%s:%u Err: Failed to create OD Query\n"
- "%s:%u Err: Failed to create OD Session\n"
- "%s:%u Err: Failed to create payload dictionary\n"
- "%s:%u Err: Failed to create session info dictionary\n"
- "%s:%u Err: Failed to create stats dictionary\n"
- "%s:%u Err: Failed to create user info dictionary\n"
- "%s:%u Err: Failed to detect fext structure version:\n"
- "%s:%u Err: Failed to detect proper IOCTL to use\n"
- "%s:%u Err: Failed to disable rapid-aging vnodes for splitter telemetry scan: %d\n"
- "%s:%u Err: Failed to enable rapid-aging vnodes for splitter telemetry scan: %d\n"
- "%s:%u Err: Failed to find users homedirs\n"
- "%s:%u Err: Failed to get OD Query results\n"
- "%s:%u Err: Failed to send splitter telemetry scan report, err: %u\n"
- "%s:%u Err: IOCTL detection failed on 0x%lx (%zu) with %u\n"
- "%s:%u Err: Inner scan has failed, most likely we ran out of memory\n"
- "%s:%u Err: Lba end (0x%llx + 0x%llx) outside of bitmap: 0x%llx > 0x%zx\n"
- "%s:%u Err: Outer namespace scan failed for [%s]: %u\n"
- "%s:%u Err: Outer namespace scan failed: %u\n"
- "%s:%u Err: Outer scan has failed, most likely we ran out of memory\n"
- "%s:%u Err: Overflow: 0x%llx + 0x%llx == 0x%llx\n"
- "%s:%u Err: ProcessFext failed for fext offs %llu of dsid %llu for %s: %u\n"
- "%s:%u Err: ProcessFile failed for %s: %u\n"
- "%s:%u Err: RTCReporting failed to send the payload and refused to even say why (error is NULL).\n"
- "%s:%u Err: RTCReporting failed to send the payload and refused to even say why. Error has no description but error code is %li.\n"
- "%s:%u Err: RTCReporting failed to send the payload. Error: %li : [%s]\n"
- "%s:%u Err: Scan section has failed, most likely we ran out of memory\n"
- "%s:%u Err: Splitter telemetry scan failed with %u and %llu shared blocks found so far, sending report\n"
- "%s:%u Err: failed set splitter telemetry xpc activity state to %s\n"
- "%s:%u Err: fsctl(APFSIOC_DEBUG_STATS) failed for dstream of %s : %u\n"
- "%s:%u Err: fsctl(APFSIOC_DEBUG_STATS) failed for fexts of dsid %llu for %s: %u\n"
- "%s:%u Err: fts_open() for %s failed with %u\n"
- "%s:%u Err: fts_read() failed with %u\n"
- "... Skipping [%s]\n"
- "... home dir [%s]\n"
- "/.Trash/"
- "/Applications/"
- "/Applications/Xcode"
- "/Downloads/"
- "/Library/"
- "/Library/Application Support/"
- "/Library/Caches/"
- "/Library/Containers/"
- "/Library/Developer/"
- "/Library/Group Containers/"
- "/Library/Mail/"
- "/Library/Messages/"
- "/Library/Metadata/"
- "/Library/Photos/"
- "/Music/"
- "/Pictures/"
- "/System"
- "/Volumes"
- "/dev"
- "/private/var"
- "/private/var/"
- "/private/var/log/"
- "/private/var/root/Library/Caches/"
- "/tmp/"
- "3288.1.3"
- "Alloc bitmap for %zu entries, %zu bit(s) per entry, %zu bytes\n"
- "Applications"
- "ApplicationsXCode"
- "Cat: %3u blocks %9llu\t"
- "Category_%d"
- "Creating splitter_telemetry_report log"
- "D:dfht"
- "DEFER"
- "DONE"
- "Default"
- "Detected IOCTL as 0x%lx (%zu)\n"
- "Disabled rapid-aging vnodes for splitter telemetry scan\n"
- "Enabled rapid-aging vnodes for splitter telemetry scan\n"
- "Finished splitter telemetry scan with %llu shared blocks found\n"
- "Finished splitter telemetry scan with %llu shared blocks found, sending report\n"
- "Initiating splitter telemetry scan"
- "Initiating splitter telemetry scan\n"
- "Library"
- "LibraryAppSupp"
- "LibraryCaches"
- "LibraryDeveloper"
- "ProcessFext"
- "QueryUserHomeDirs"
- "Run"
- "Scanning Outer...\n"
- "Scanning [%s]...\n"
- "Size"
- "Splitter telemetry scan failed with %u and %llu shared blocks found so far\n"
- "Splitter telemetry scan has been interrupted"
- "Splitter telemetry scan has been interrupted, deferring for later\n"
- "Splitter telemetry scan report has been sent\n"
- "Tmp"
- "Unknown"
- "UserDefault"
- "UserDownloads"
- "UserLibrary"
- "UserLibraryAppSupp"
- "UserLibraryCaches"
- "UserLibraryContainers"
- "UserLibraryDeveloper"
- "UserLibraryMail"
- "UserLibraryMessages"
- "UserLibraryMetadata"
- "UserLibraryPhotos"
- "UserMusic"
- "UserPictures"
- "UserTrash"
- "Using IOKit disk size (%llu) instead of statfs (%llu)\n"
- "Var"
- "VarLog"
- "basic_string"
- "collect_splitter_telemetry"
- "com.apple.apfsd.splitter_telemetry_report"
- "init_splitter_telemetry_block_invoke"
- "kern.rage_vnode"
- "numSharedBlocks"
- "scan_error"
- "send_report"
- "shared_blocks"
- "split_telemetry"
- "splitter_telemetry_report"
- "vector"
```
