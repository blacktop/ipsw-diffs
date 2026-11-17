## ANEStorageMaintainer

> `/System/Library/PrivateFrameworks/AppleNeuralEngine.framework/XPCServices/ANEStorageMaintainer.xpc/ANEStorageMaintainer`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-382.102.2.0.0
-  __TEXT.__text: 0x7e54
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x3dc
+382.200.2.0.0
+  __TEXT.__text: 0x85bc
+  __TEXT.__auth_stubs: 0x560
+  __TEXT.__objc_stubs: 0x1140
+  __TEXT.__objc_methlist: 0x424
   __TEXT.__const: 0xc8
-  __TEXT.__oslogstring: 0xfec
-  __TEXT.__objc_classname: 0x86
-  __TEXT.__objc_methname: 0x1075
-  __TEXT.__objc_methtype: 0x26b
-  __TEXT.__cstring: 0x1d0
-  __TEXT.__unwind_info: 0x1f0
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__cfstring: 0x320
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__oslogstring: 0x1025
+  __TEXT.__objc_classname: 0x9b
+  __TEXT.__objc_methname: 0x116b
+  __TEXT.__objc_methtype: 0x279
+  __TEXT.__cstring: 0x1df
+  __TEXT.__unwind_info: 0x200
+  __DATA_CONST.__const: 0xd0
+  __DATA_CONST.__cfstring: 0x380
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x2b0
-  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__objc_const: 0x450
-  __DATA.__objc_selrefs: 0x520
+  __DATA.__objc_const: 0x4e0
+  __DATA.__objc_selrefs: 0x590
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x140
+  __DATA.__objc_data: 0x190
   __DATA.__data: 0x130
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 112
-  Symbols:   392
-  CStrings:  338
+  Functions: 123
+  Symbols:   422
+  CStrings:  359
 
Symbols:
+ +[_ANECacheMaintenance accessTimeForPath:]
+ +[_ANECacheMaintenance isPath:safelyWithinDirectory:]
+ +[_ANECacheMaintenance removeEntriesAtPath:notAccessedFor:]
+ +[_ANECacheMaintenance setAccessTime:forPath:]
+ +[_ANECacheMaintenance updateAccessTimeForPath:]
+ /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Binaries/AppleNeuralEngine_CompilerService/install/TempContent/Objects/AppleNeuralEngine.build/ANEStorageMaintainer.build/Objects-normal/arm64e/_ANECacheMaintenance.o
+ _ANECacheMaintenance.m
+ _ANEStandardizedPath
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$__ANECacheMaintenance
+ _OBJC_METACLASS_$__ANECacheMaintenance
+ __OBJC_$_CLASS_METHODS__ANECacheMaintenance
+ __OBJC_CLASS_RO_$__ANECacheMaintenance
+ __OBJC_METACLASS_RO_$__ANECacheMaintenance
+ _kANECacheTrashDirectoryName
+ _objc_msgSend$UUID
+ _objc_msgSend$UUIDString
+ _objc_msgSend$accessTimeForPath:
+ _objc_msgSend$array
+ _objc_msgSend$common
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$count
+ _objc_msgSend$date
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$insertObject:atIndex:
+ _objc_msgSend$isPath:safelyWithinDirectory:
+ _objc_msgSend$setAccessTime:forPath:
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$updateAccessTimeForPath:
+ _rename
- _objc_msgSend$setAccessTime:forModelFilePath:
CStrings:
+ "%@-%@"
+ "%@: Skipping update for path=%@"
+ "%@: could not move %@ to trash : errno=%d"
+ "%@: could not remove %@ : error=%@"
+ "%@: getxattr(%@, %@) failed : errno=%d"
+ "%@: getxattr(%@, %@) missing attribute"
+ "%@: nothing to reclaim at %@ : error=%@"
+ "%@: removed %lu of %lu entries from %@"
+ "%@: setxattr(%@, %@) failed : errno=%d"
+ "."
+ ".trash"
+ "UUID"
+ "UUIDString"
+ "_ANECacheMaintenance"
+ "accessTimeForPath:"
+ "array"
+ "common"
+ "contentsOfDirectoryAtPath:error:"
+ "count"
+ "date"
+ "fileSystemRepresentation"
+ "insertObject:atIndex:"
+ "removeEntriesAtPath:notAccessedFor:"
+ "setAccessTime:forPath:"
+ "timeIntervalSinceDate:"
+ "updateAccessTimeForPath:"
+ "v32@0:8@16d24"
- "%@: +setAccessTime:forFilePath failed"
- "%@: Skipping update for filePath=%@"
- "%@: filePath=%@"
- "%@: getxattr(%@, %@, %p, %lu) failed  : errno=%d"
- "%@: getxattr(%@, %@, %p, %lu) missing attribute  : errno=%d"
- "%@: setxattr(%@, %@, %p, %lu) failed  : errno=%d"
```
