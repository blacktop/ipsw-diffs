## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-455.30.6.9.8
-  __TEXT.__text: 0x2185c
+455.30.6.9.11
+  __TEXT.__text: 0x2229c
   __TEXT.__auth_stubs: 0x460
-  __TEXT.__objc_methlist: 0x26fc
+  __TEXT.__objc_methlist: 0x2744
   __TEXT.__const: 0xb8
-  __TEXT.__oslogstring: 0x28e3
-  __TEXT.__cstring: 0x3fd4
+  __TEXT.__oslogstring: 0x2a5c
+  __TEXT.__cstring: 0x40a8
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__unwind_info: 0x7b8
+  __TEXT.__unwind_info: 0x7c8
   __TEXT.__objc_classname: 0x63d
-  __TEXT.__objc_methname: 0x4f75
-  __TEXT.__objc_methtype: 0x11b0
-  __TEXT.__objc_stubs: 0x36c0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x1198
+  __TEXT.__objc_methname: 0x5073
+  __TEXT.__objc_methtype: 0x11f4
+  __TEXT.__objc_stubs: 0x3780
+  __DATA_CONST.__got: 0x188
+  __DATA_CONST.__const: 0x11a0
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1250
+  __DATA_CONST.__objc_selrefs: 0x12a0
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x110
   __AUTH_CONST.__auth_got: 0x240
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x3ae0
-  __AUTH_CONST.__objc_const: 0x7260
+  __AUTH_CONST.__cfstring: 0x3bc0
+  __AUTH_CONST.__objc_const: 0x7270
+  __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x6e0
   __DATA.__objc_ivar: 0x21c
   __DATA.__data: 0x970

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 08AD5470-C56A-35D7-A56A-62E33744D189
-  Functions: 981
-  Symbols:   3905
-  CStrings:  2363
+  UUID: 32F55358-6EFA-3B86-9F2A-308A893B5AFB
+  Functions: 988
+  Symbols:   3936
+  CStrings:  2400
 
Symbols:
+ -[FMDSharedConfiguration clearFindMySignOutTimeFile]
+ -[FMDSharedConfiguration clearFindMySignOutTimeFile].cold.1
+ -[FMDSharedConfiguration clearFindMySignOutTimeFile].cold.2
+ -[FMDSharedConfiguration postTheftAndLossCFUWithEntry:reply:]
+ -[FMDSharedConfiguration readFindMySignOutTimeFromFile]
+ -[FMDSharedConfiguration readFindMySignOutTimeFromFile].cold.1
+ -[FMDSharedConfiguration signOutTimestampFileURL]
+ -[FMDSharedConfiguration signOutTimestampFileURL].cold.1
+ -[FMDSharedConfiguration signOutTimestampFileURL].cold.2
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile]
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile].cold.1
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile].cold.2
+ -[FMDSharedConfiguration writeFindMySignOutTimeToFile].cold.3
+ _NSURLIsExcludedFromBackupKey
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ ___61-[FMDSharedConfiguration postTheftAndLossCFUWithEntry:reply:]_block_invoke
+ ___61-[FMDSharedConfiguration postTheftAndLossCFUWithEntry:reply:]_block_invoke_2
+ _kFMDCoreFollowUpTheftAndLossReminderSignOutTimestampKey
+ _objc_msgSend$date
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$postTheftAndLossCFUWithEntry:reply:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$setResourceValue:forKey:error:
+ _objc_msgSend$signOutTimestampFileURL
- -[FMDSharedConfiguration requestTheftAndLossCFUWithStrings:andReply:]
- ___69-[FMDSharedConfiguration requestTheftAndLossCFUWithStrings:andReply:]_block_invoke
- ___69-[FMDSharedConfiguration requestTheftAndLossCFUWithStrings:andReply:]_block_invoke_2
- _objc_msgSend$requestTheftAndLossCFUWithStrings:andReply:
CStrings:
+ "Error excluding %@ from backup %@"
+ "Failed to read contents with error: %@"
+ "Failed to remove file (%@) with error %@."
+ "Failed to write the timestamp to %@ with error %@."
+ "Failure to request a CFU with error: %@, shouldEnable: %{public}@"
+ "Invalid URL (%@) for the timestamp file."
+ "No CFU requested"
+ "No contents"
+ "No record of the last sign out. Bailing."
+ "Removed (%@)."
+ "SignOutTimestamp"
+ "TNL_REMINDER_INFORMATIVE_TEXT_DEFAULT"
+ "TNL_REMINDER_MESSAGE_DEFAULT"
+ "TNL_REMINDER_SUBTITLE_TEXT_DEFAULT"
+ "TNL_REMINDER_TITLE_DEFAULT"
+ "Wrote (%@) to (%@)."
+ "clearFindMySignOutTimeFile"
+ "date"
+ "fileExistsAtPath:isDirectory:"
+ "group.com.apple.icloud.findmydevice.followup"
+ "lastPathComponent"
+ "postTheftAndLossCFUWithEntry:reply:"
+ "readFindMySignOutTimeFromFile"
+ "removeItemAtPath:error:"
+ "setResourceValue:forKey:error:"
+ "signOutTimestampFileURL"
+ "theftandloss.plist"
+ "v32@0:8@\"FMDSharedConfigurationFollowUpEntry\"16@?<v@?B@\"NSError\">24"
+ "writeFindMySignOutTimeToFile"

```
