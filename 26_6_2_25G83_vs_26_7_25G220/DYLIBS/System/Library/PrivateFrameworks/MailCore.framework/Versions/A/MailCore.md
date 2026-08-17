## MailCore

> `/System/Library/PrivateFrameworks/MailCore.framework/Versions/A/MailCore`

```diff

-3864.700.51.1.1
-  __TEXT.__text: 0x8a8d0
-  __TEXT.__auth_stubs: 0x1210
-  __TEXT.__objc_methlist: 0x80e4
-  __TEXT.__const: 0x4a0
-  __TEXT.__cstring: 0x7dc3
+3864.700.51.1.3
+  __TEXT.__text: 0x8b764
+  __TEXT.__auth_stubs: 0x1230
+  __TEXT.__objc_methlist: 0x812c
+  __TEXT.__const: 0x4b0
+  __TEXT.__cstring: 0x7f41
   __TEXT.__gcc_except_tab: 0x1650
-  __TEXT.__oslogstring: 0x1c2e
-  __TEXT.__unwind_info: 0x2328
-  __TEXT.__objc_classname: 0xdd0
-  __TEXT.__objc_methname: 0x144ab
-  __TEXT.__objc_methtype: 0x2b93
-  __TEXT.__objc_stubs: 0x10880
-  __DATA_CONST.__got: 0x1108
+  __TEXT.__oslogstring: 0x1de7
+  __TEXT.__unwind_info: 0x2350
+  __TEXT.__objc_classname: 0xdef
+  __TEXT.__objc_methname: 0x1460b
+  __TEXT.__objc_methtype: 0x2ba4
+  __TEXT.__objc_stubs: 0x109c0
+  __DATA_CONST.__got: 0x1118
   __DATA_CONST.__const: 0x1208
-  __DATA_CONST.__objc_classlist: 0x360
+  __DATA_CONST.__objc_classlist: 0x368
   __DATA_CONST.__objc_catlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5420
+  __DATA_CONST.__objc_selrefs: 0x5478
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x1a0
-  __AUTH_CONST.__auth_got: 0x918
-  __AUTH_CONST.__const: 0x1370
-  __AUTH_CONST.__cfstring: 0x9040
-  __AUTH_CONST.__objc_const: 0xca80
+  __AUTH_CONST.__auth_got: 0x928
+  __AUTH_CONST.__const: 0x1390
+  __AUTH_CONST.__cfstring: 0x9160
+  __AUTH_CONST.__objc_const: 0xcb10
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH.__objc_data: 0xaa0
+  __AUTH.__objc_data: 0xaf0
   __DATA.__objc_ivar: 0x798
   __DATA.__data: 0xdb0
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x208
   __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__bss: 0x3f0
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2871
-  Symbols:   7573
-  CStrings:  5540
+  Functions: 2884
+  Symbols:   7602
+  CStrings:  5571
 
Symbols:
+ +[MCAppleScriptSandboxValidation _senderOfCommand:passesSandboxAuditForPath:forWriting:]
+ +[MCAppleScriptSandboxValidation isPathInsideMailContainer:]
+ +[MCAppleScriptSandboxValidation isSendToSelfEvent:]
+ +[MCAppleScriptSandboxValidation senderOfCommand:passesSandboxAuditToReadFromURL:]
+ +[MCAppleScriptSandboxValidation senderOfCommand:passesSandboxAuditToWriteToURL:]
+ _NSHomeDirectory
+ _OBJC_CLASS_$_MCAppleScriptSandboxValidation
+ _OBJC_METACLASS_$_MCAppleScriptSandboxValidation
+ _SANDBOX_CHECK_NO_REPORT
+ __FourCharCodeString
+ __OBJC_$_CLASS_METHODS_MCAppleScriptSandboxValidation
+ __OBJC_CLASS_RO_$_MCAppleScriptSandboxValidation
+ __OBJC_METACLASS_RO_$_MCAppleScriptSandboxValidation
+ ____appleScriptSecurityLog_block_invoke
+ __appleScriptSecurityLog
+ _appleScriptSecurityLog
+ _appleScriptSecurityLog.log
+ _appleScriptSecurityLog.onceToken
+ _objc_msgSend$URLByDeletingLastPathComponent
+ _objc_msgSend$URLByResolvingSymlinksInPath
+ _objc_msgSend$URLByStandardizingPath
+ _objc_msgSend$_senderOfCommand:passesSandboxAuditForPath:forWriting:
+ _objc_msgSend$eventClass
+ _objc_msgSend$eventID
+ _objc_msgSend$getRelationship:ofDirectoryAtURL:toItemAtURL:error:
+ _objc_msgSend$isPathInsideMailContainer:
+ _objc_msgSend$isSendToSelfEvent:
+ _objc_msgSend$senderOfCommand:passesSandboxAuditToWriteToURL:
+ _sandbox_check_by_audit_token
CStrings:
+ "????"
+ "AppleScriptSecurity"
+ "B36@0:8@16@24B32"
+ "Blocked AppleScript access to protected path (prefix match): %{private}s"
+ "Blocked AppleScript access to protected path: %{private}s"
+ "Cannot save attachments sourced from Mail's private data directories."
+ "Cannot save attachments to Mail's private data directories."
+ "Denied AppleScript %{public}s [%{public}@/%{public}@]: invalid audit token size for path: %{private}s"
+ "Denied AppleScript %{public}s [%{public}@/%{public}@]: no sender audit token for path: %{private}s"
+ "Denied AppleScript %{public}s [%{public}@/%{public}@]: sender lacks sandbox permission for path: %{private}s"
+ "Library/Accounts"
+ "Library/Application Support/Mail"
+ "Library/Containers/com.apple.mail"
+ "Library/Mail"
+ "Library/Suggestions"
+ "MCAppleScriptSandboxValidation"
+ "The sender does not have permission to write to the specified path."
+ "URLByDeletingLastPathComponent"
+ "URLByResolvingSymlinksInPath"
+ "URLByStandardizingPath"
+ "_senderOfCommand:passesSandboxAuditForPath:forWriting:"
+ "eventClass"
+ "eventID"
+ "file-read-data"
+ "file-write-data"
+ "getRelationship:ofDirectoryAtURL:toItemAtURL:error:"
+ "isPathInsideMailContainer:"
+ "isSendToSelfEvent:"
+ "senderOfCommand:passesSandboxAuditToReadFromURL:"
+ "senderOfCommand:passesSandboxAuditToWriteToURL:"
+ "write"
```
