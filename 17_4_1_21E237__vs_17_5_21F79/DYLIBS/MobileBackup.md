## MobileBackup

> `/System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup`

```diff

-2125.102.2.0.0
-  __TEXT.__text: 0x42538
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x4894
+2125.120.44.0.1
+  __TEXT.__text: 0x420f8
+  __TEXT.__auth_stubs: 0xf30
+  __TEXT.__objc_methlist: 0x4884
   __TEXT.__const: 0x590
-  __TEXT.__cstring: 0xc381
-  __TEXT.__oslogstring: 0x3c86
-  __TEXT.__gcc_except_tab: 0x1580
-  __TEXT.__unwind_info: 0x14e8
+  __TEXT.__cstring: 0xc3f9
+  __TEXT.__oslogstring: 0x3cdb
+  __TEXT.__gcc_except_tab: 0x1520
+  __TEXT.__unwind_info: 0x14dc
   __TEXT.__objc_classname: 0x4a6
-  __TEXT.__objc_methname: 0xbc50
-  __TEXT.__objc_methtype: 0x151d
-  __TEXT.__objc_stubs: 0x6120
+  __TEXT.__objc_methname: 0xbca0
+  __TEXT.__objc_methtype: 0x1542
+  __TEXT.__objc_stubs: 0x6180
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0x848
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x50b8
+  __DATA_CONST.__objc_const: 0x50c8
   __DATA_CONST.__objc_selrefs: 0x2940
   __DATA_CONST.__objc_classrefs: 0x2e8
   __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0xa0
-  __AUTH_CONST.__cfstring: 0x6900
+  __AUTH_CONST.__cfstring: 0x6920
   __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x7b0
+  __AUTH_CONST.__auth_got: 0x7a8
   __DATA.__objc_ivar: 0x400
   __DATA.__data: 0x3c0
   __DATA.__bss: 0x1f8
-  __DATA_DIRTY.__const: 0x520
+  __DATA_DIRTY.__const: 0x540
   __DATA_DIRTY.__objc_const: 0x1b00
   __DATA_DIRTY.__objc_data: 0x1130
   __DATA_DIRTY.__data: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1891
-  Symbols:   5933
-  CStrings:  4034
+  Functions: 1886
+  Symbols:   5922
+  CStrings:  4039
 
Symbols:
+ +[MBFileInfo fileInfoWithAbsolutePath:mode:priority:]
+ +[MBFileInfo fileInfoWithRestorable:]
+ -[MBBehaviorOptions requiredRestoreSnapshotFormatString]
+ -[MBBehaviorOptions shouldVerifyRestore]
+ -[MBFileInfo _initWithAbsolutePath:extendedAttributes:isDirectory:priority:]
+ -[NSFileManager(MobileBackup) mb_moveAsideAndMarkAsPurgeableItemAtPath:error:]
+ -[NSFileManager(MobileBackup) mb_moveAsideAndMarkAsPurgeableItemAtPath:error:].cold.1
+ ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.109
+ _objc_msgSend$_initWithAbsolutePath:extendedAttributes:isDirectory:priority:
+ _objc_msgSend$absolutePath
+ _objc_msgSend$extendedAttributes
+ _objc_msgSend$iso8601String
+ _objc_msgSend$priority
+ _objc_msgSend$type
- +[MBFileInfo fileInfoWithPath:extendedAttributes:]
- -[MBBehaviorOptions syntheticATCPathPrefix]
- -[MBFileInfo initWithPath:extendedAttributes:]
- -[MBFileInfo setExtendedAttributes:]
- -[MBFileInfo setIsDirectory:]
- -[MBFileInfo setPath:]
- -[MBFileInfo setPriority:]
- -[NSFileManager(MobileBackup) mb_markItemPurgeableAtPath:error:]
- -[NSFileManager(MobileBackup) mb_markItemPurgeableAtPath:error:].cold.1
- GCC_except_table17
- ___52-[MBBehaviorOptions _startListeningForNotifications]_block_invoke.106
- ___54-[MBBehaviorOptions _getIntOptionForKey:defaultValue:]_block_invoke
- ___55-[MBBehaviorOptions _getBoolOptionForKey:defaultValue:]_block_invoke
- ___57-[MBBehaviorOptions _getDoubleOptionForKey:defaultValue:]_block_invoke
- _objc_msgSend$initWithPath:extendedAttributes:
- _objc_msgSend$setIsDirectory:
- _objc_msgSend$setPriority:
- _stat
CStrings:
+ "-[NSFileManager(MobileBackup) mb_moveAsideAndMarkAsPurgeableItemAtPath:error:]"
+ "=mbfm= ma: Unable to move aside (%{public}@) to (%{public}@): %@"
+ "=mbfm= mg: Cleaning up un-migrated (%{public}@) from %{public}@, already present in %{public}@"
+ "=mbfm= mg: Migrating (%{public}@) from %{public}@ to %{public}@"
+ "=mbfm= mg: Nothing to migrate from %{public}@ to %{public}@"
+ "=mbfm= mg: Nothing to migrate from %{public}@, already present in %{public}@"
+ "=mbfm= rm: Attempting to remove (%{public}@) in place"
+ "=mbfm= rm: Nothing at %{public}@ to remove"
+ "=mbfm= rm: Nothing at (%{public}@) to move to temporary cleanup dir (%{public}@)"
+ "=mbfm= rm: Removing temporary cleanup dir (%{public}@)"
+ "=mbfm= rm: Unable to create temporary cleanup dir: %{public}@"
+ "=mbfm= rm: Unable to move (%{public}@) to temporary cleanup dir (%{public}@): %@"
+ "@36@0:8@16S24Q28"
+ "@44@0:8@16@24B32Q36"
+ "RequiredRestoreSnapshotFormat"
+ "T@\"NSDictionary\",R,C,N,V_extendedAttributes"
+ "T@\"NSString\",R,C,N,V_path"
+ "TB,R,N,V_isDirectory"
+ "TQ,R,N,V_priority"
+ "VerifyRestore"
+ "_initWithAbsolutePath:extendedAttributes:isDirectory:priority:"
+ "absolutePath"
+ "fileInfoWithAbsolutePath:mode:priority:"
+ "fileInfoWithRestorable:"
+ "iso8601String"
+ "mb_moveAsideAndMarkAsPurgeableItemAtPath:error:"
+ "requiredRestoreSnapshotFormatString"
+ "shouldVerifyRestore"
- "-[NSFileManager(MobileBackup) mb_markItemPurgeableAtPath:error:]"
- "MBFM-mg: Cleaning up un-migrated (%{public}@) from %{public}@, already present in %{public}@"
- "MBFM-mg: Migrating (%{public}@) from %{public}@ to %{public}@"
- "MBFM-mg: Nothing to migrate from %{public}@ to %{public}@"
- "MBFM-mg: Nothing to migrate from %{public}@, already present in %{public}@"
- "MBFM-rm: Attempting to remove (%{public}@) in place"
- "MBFM-rm: Nothing at %{public}@ to remove"
- "MBFM-rm: Nothing at (%{public}@) to move to temporary cleanup dir (%{public}@)"
- "MBFM-rm: Removing temporary cleanup dir (%{public}@)"
- "MBFM-rm: Unable to create temporary cleanup dir: %{public}@"
- "MBFM-rm: Unable to move (%{public}@) to temporary cleanup dir (%{public}@): %@"
- "SyntheticATCPathPrefix"
- "T@\"NSDictionary\",C,N,V_extendedAttributes"
- "T@\"NSString\",C,N,V_path"
- "TB,N,V_isDirectory"
- "Tq,N,V_priority"
- "fileInfoWithPath:extendedAttributes:"
- "initWithPath:extendedAttributes:"
- "mb_markItemPurgeableAtPath:error:"
- "setExtendedAttributes:"
- "setIsDirectory:"
- "setPath:"
- "setPriority:"
- "syntheticATCPathPrefix"

```
