## brctl

> `/usr/bin/brctl`

```diff

-3097.81.2.0.0
-  __TEXT.__text: 0x16978
-  __TEXT.__auth_stubs: 0xa90
+3437.101.1.0.0
+  __TEXT.__text: 0x167d8
+  __TEXT.__auth_stubs: 0xa80
   __TEXT.__objc_stubs: 0x30a0
-  __TEXT.__objc_methlist: 0x60c
-  __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x954
+  __TEXT.__objc_methlist: 0x7ac
+  __TEXT.__const: 0x100
+  __TEXT.__gcc_except_tab: 0x94c
   __TEXT.__objc_classname: 0xda
-  __TEXT.__objc_methname: 0x2a34
+  __TEXT.__objc_methname: 0x2ab0
   __TEXT.__objc_methtype: 0x42d
-  __TEXT.__cstring: 0x472f
-  __TEXT.__oslogstring: 0x102
-  __TEXT.__unwind_info: 0x3f8
-  __DATA_CONST.__auth_got: 0x558
-  __DATA_CONST.__got: 0x488
-  __DATA_CONST.__const: 0x1038
+  __TEXT.__cstring: 0x47e8
+  __TEXT.__oslogstring: 0xd6
+  __TEXT.__unwind_info: 0x400
+  __DATA_CONST.__auth_got: 0x550
+  __DATA_CONST.__got: 0x490
+  __DATA_CONST.__const: 0x1048
   __DATA_CONST.__cfstring: 0x2520
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_arraydata: 0x140
-  __DATA_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_arraydata: 0x118
+  __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1738
-  __DATA.__objc_selrefs: 0xcb0
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_const: 0x14f8
+  __DATA.__objc_selrefs: 0xd60
+  __DATA.__objc_ivar: 0x150
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x1c8
-  __DATA.__bss: 0x68
+  __DATA.__data: 0x1e0
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 7CCA1BCC-720F-3A52-947B-358F2886E7F6
-  Functions: 288
+  UUID: 883A27FC-41F9-35CF-AF8C-A0F776C8E5B0
+  Functions: 286
   Symbols:   328
-  CStrings:  1626
+  CStrings:  1627
 
Symbols:
+ _OBJC_CLASS_$_BRSpecialFolders
- _BRIsFPFSEnabled
CStrings:
+ "                         wait for at least one item that has an uploading progress"
+ "    -u,--wait-start-uploading"
+ "    disable               disables spotlight indexing"
+ "    enable                enables spotlight indexing"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/brctl/brctl.m"
+ "/AppleInternal/Library/BuildRoots/656826c2-0194-11f0-9fc9-122ba06eff56/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/brctl/cmd-diagnose.m"
+ "/bin/launchctl start com.apple.bird"
+ "/usr/bin/defaults write com.apple.bird spotlight-indexer.enabled -bool %s"
+ "/usr/bin/pkill -KILL bird"
+ "/usr/bin/pkill -STOP bird"
+ "Dropped Spotlight index successfully"
+ "Logs/CrashReporter/DiagnosticLogs/com.apple.corespotlight.asl"
+ "Spotlight indexing has been enabled"
+ "Stopping the query because at least one item started uploading"
+ "Stopping the query since the timeout has elapsed\n"
+ "T@\"NSString\",&,N,V_focusedFile"
+ "Unable to drop Spotlight Index: %s"
+ "_focusedFile"
+ "_startedUploading"
+ "_waitForStartUploading"
+ "a"
+ "coreSpotlightLogPath"
+ "disable"
+ "dropSpotlightIndexWithReply:"
+ "enable"
+ "focusedFile"
+ "fp_isFolder"
+ "gipt:S:wu"
+ "homeDirForCurrentPersona"
+ "setFocusedFile:"
+ "spotlight"
+ "spotlight [<command>]"
+ "taskWithCommandWithArguments:"
+ "wait-start-uploading"
- "    FPFS Feature: %s\n"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/brctl/brctl.m"
- "/AppleInternal/Library/BuildRoots/423aabcf-bd7b-11ef-ae7d-aabfac210453/Library/Caches/com.apple.xbs/Sources/CloudDocs_executables/brctl/cmd-diagnose.m"
- "/System/Library/PrivateFrameworks/CloudDocsDaemon.framework/CloudDocsDaemon"
- "BRCAccountSessionFPFS"
- "Can't create the fpfs sync proxy when fpfs isn't enabled"
- "Can't open CloudDocsDaemon"
- "CloudDocsDaemonLibrary"
- "Disabled"
- "Enabled"
- "Stopping the query since the specified time has elapsed"
- "[WARNING] Can't open CloudDocsDaemon : %s%@"
- "br_addPhysicalProperty"
- "br_currentHomeDir"
- "classBRCAccountSessionFPFS"
- "failed getting lookup info at '%s': %s\n"
- "gatherInformationForPath:reply:"
- "gipt:S:w"
- "initBRCAccountSessionFPFS"
- "local item"
- "local path match"
- "longLongValue"
- "newLegacySyncProxy"
- "relpath"
- "server item"
- "server path match"
- "timed out getting lookup info at '%s'\n"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "┏"
- "┗"
- "┣"
- "┳"

```
