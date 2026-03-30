## GamePolicy

> `/System/Library/PrivateFrameworks/GamePolicy.framework/GamePolicy`

```diff

-3.4.4.0.0
-  __TEXT.__text: 0x18ee0
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0xe3c
-  __TEXT.__const: 0xf20
-  __TEXT.__cstring: 0xd56
-  __TEXT.__gcc_except_tab: 0x6c
+3.5.1.0.0
+  __TEXT.__text: 0x1b6c8
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_methlist: 0xec4
+  __TEXT.__const: 0xf80
+  __TEXT.__cstring: 0xdd1
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__oslogstring: 0x48e
   __TEXT.__dlopen_cstrs: 0x66
-  __TEXT.__oslogstring: 0x1d3
-  __TEXT.__swift5_typeref: 0x597
-  __TEXT.__swift5_fieldmd: 0x67c
-  __TEXT.__constg_swiftt: 0xd70
+  __TEXT.__swift5_typeref: 0x605
+  __TEXT.__swift5_fieldmd: 0x6d4
+  __TEXT.__constg_swiftt: 0xdfc
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x548
+  __TEXT.__swift5_reflstr: 0x5ce
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x78
-  __TEXT.__swift5_types: 0x8c
+  __TEXT.__swift5_types: 0x90
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x988
-  __TEXT.__eh_frame: 0x80
-  __TEXT.__objc_classname: 0x7f6
-  __TEXT.__objc_methname: 0x18bf
-  __TEXT.__objc_methtype: 0x8ab
-  __TEXT.__objc_stubs: 0xc20
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x590
-  __DATA_CONST.__objc_classlist: 0x108
+  __TEXT.__swift5_capture: 0x84
+  __TEXT.__unwind_info: 0xa70
+  __TEXT.__eh_frame: 0xf8
+  __TEXT.__objc_classname: 0x82b
+  __TEXT.__objc_methname: 0x1af1
+  __TEXT.__objc_methtype: 0x900
+  __TEXT.__objc_stubs: 0xd20
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0x5a0
+  __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__objc_selrefs: 0x548
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x648
-  __AUTH_CONST.__const: 0x5b0
-  __AUTH_CONST.__cfstring: 0x260
-  __AUTH_CONST.__objc_const: 0x21f8
+  __AUTH_CONST.__auth_got: 0x708
+  __AUTH_CONST.__const: 0x740
+  __AUTH_CONST.__cfstring: 0x280
+  __AUTH_CONST.__objc_const: 0x2358
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH.__objc_data: 0x1480
-  __AUTH.__data: 0x6b8
-  __DATA.__objc_ivar: 0x40
-  __DATA.__data: 0x538
+  __AUTH.__objc_data: 0x15b8
+  __AUTH.__data: 0x6e0
+  __DATA.__objc_ivar: 0x48
+  __DATA.__data: 0x598
   __DATA.__bss: 0xed0
   __DATA_DIRTY.__objc_data: 0x3f8
   __DATA_DIRTY.__data: 0x128

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4955C289-728F-30B3-8828-3806953C3539
-  Functions: 1132
-  Symbols:   1058
-  CStrings:  479
+  UUID: 03AE2C34-057D-31CB-B039-8D5F9CC633BD
+  Functions: 1200
+  Symbols:   1163
+  CStrings:  518
 
Symbols:
+ +[GPGameCenterMediator gameDidBecomeForeground:auditToken:]
+ +[GPGameCenterMediator gameDidBecomeForeground:auditToken:].cold.1
+ +[GPGameCenterMediator gameDidBecomeForeground:auditToken:].cold.2
+ -[GPGameLibrary _handleXPCConnectionInterrupted]
+ -[GPGameLibrary _handleXPCConnectionInterrupted].cold.1
+ -[GPGameLibrary _handleXPCConnectionInvalidated]
+ -[GPGameLibrary _handleXPCConnectionInvalidated].cold.1
+ -[GPGameLibrary _onqueue_attemptReconnect]
+ -[GPGameLibrary _onqueue_attemptReconnect].cold.1
+ -[GPGameLibrary _onqueue_attemptReconnect].cold.2
+ -[GPGameLibrary _onqueue_resetAndScheduleReconnect]
+ -[GPGameLibrary _onqueue_resetAndScheduleReconnect].cold.1
+ -[GameMetadataHints initWithDisplayName:executableURL:isThirdPartyInstalled:]
+ -[GameMetadataHints isThirdPartyInstalled]
+ GCC_except_table10
+ GCC_except_table11
+ GCC_except_table47
+ _OBJC_CLASS_$__TtC10GamePolicy24GPGameLibraryReconnector
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_IVAR_$_GPGameLibrary._reconnector
+ _OBJC_IVAR_$_GameMetadataHints._isThirdPartyInstalled
+ _OBJC_METACLASS_$__TtC10GamePolicy24GPGameLibraryReconnector
+ _OUTLINED_FUNCTION_5
+ __DATA__TtC10GamePolicy24GPGameLibraryReconnector
+ __INSTANCE_METHODS__TtC10GamePolicy24GPGameLibraryReconnector
+ __IVARS__TtC10GamePolicy24GPGameLibraryReconnector
+ __METACLASS_DATA__TtC10GamePolicy24GPGameLibraryReconnector
+ ___21-[GPGameLibrary pong]_block_invoke
+ ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke_2
+ ___48-[GPGameLibrary _handleXPCConnectionInterrupted]_block_invoke
+ ___51-[GPGameLibrary _onqueue_resetAndScheduleReconnect]_block_invoke
+ ___58-[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]_block_invoke.13
+ ___58-[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]_block_invoke.13.cold.1
+ ___58-[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]_block_invoke.14
+ ___58-[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]_block_invoke.cold.1
+ ___block_literal_global.16
+ __os_log_debug_impl
+ __os_log_error_impl
+ _block_copy_helper.27
+ _block_copy_helper.36
+ _block_descriptor.29
+ _block_descriptor.38
+ _block_destroy_helper.28
+ _block_destroy_helper.37
+ _exp2
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_msgSend$_handleXPCConnectionInterrupted
+ _objc_msgSend$_handleXPCConnectionInvalidated
+ _objc_msgSend$_onqueue_attemptReconnect
+ _objc_msgSend$_onqueue_resetAndScheduleReconnect
+ _objc_msgSend$gameDidLaunch:auditToken:
+ _objc_msgSend$initWithDisplayName:executableURL:isThirdPartyInstalled:
+ _objc_msgSend$isThirdPartyInstalled
+ _objc_msgSend$reset
+ _objc_msgSend$scheduleReconnectOn:execute:
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_isEscapingClosureAtFileLocation
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_stdlib_random
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic Ieg_
+ _symbolic IeyB_
+ _symbolic Ig_
+ _symbolic Say_____G 10Foundation4DateV
+ _symbolic Say_____G 8Dispatch0A13WorkItemFlagsV
+ _symbolic So17OS_dispatch_queueC
+ _symbolic _____ 10GamePolicy24GPGameLibraryReconnectorC
+ _symbolic _____SgXw 10GamePolicy24GPGameLibraryReconnectorC
+ _symbolic _____SgXwz_Xx 10GamePolicy24GPGameLibraryReconnectorC
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4DateV
+ _symbolic ytSg
- GCC_except_table39
- ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.7
- ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.7.cold.1
- ___45-[GPGameLibrary _onqueue_connectToXPCService]_block_invoke.cold.1
- ___58-[GPGameLibrary fetchInstalledGamesWithCompletionHandler:]_block_invoke_2
- ___block_literal_global.14
- _objc_msgSend$initWithDisplayName:executableURL:
CStrings:
+ "-[GKUtilityService gameDidLaunch:auditToken:] not yet available: %@"
+ "@\"_TtC10GamePolicy24GPGameLibraryReconnector\""
+ "@36@0:8@16@24B32"
+ "B32@0:8@16@?24"
+ "Crash loop detected in gamepolicyd. Permenantly invalidating the connection."
+ "FetchInstalledGamesWithCompletionHandler: got %lu games from gamepolicyd"
+ "GPGameLibrary: Attempting reconnect..."
+ "GPGameLibrary: Crash loop detected..."
+ "GPGameLibrary: Reconnect aborted — permanently invalidated."
+ "GPGameLibrary: Reconnect already pending, skipping duplicate."
+ "GPGameLibrary: Scheduling reconnect attempt %ld in %fs."
+ "GPGameLibrary: XPC connection interrupted. Scheduling reconnect."
+ "GPGameLibrary: XPC connection invalidated."
+ "GPGameLibrary: library not yet initialized, fetching directly from gamepolicyd."
+ "GPGameLibrary: pong! Connection to gamepolicyd confirmed."
+ "GPGameLibraryReconnector.stateQ"
+ "IsLauncherAndGame"
+ "TB,R,N,V_isThirdPartyInstalled"
+ "_TtC10GamePolicy24GPGameLibraryReconnector"
+ "_attemptCount"
+ "_attemptTimestamps"
+ "_handleXPCConnectionInterrupted"
+ "_handleXPCConnectionInvalidated"
+ "_isPending"
+ "_isThirdPartyInstalled"
+ "_onqueue_attemptReconnect"
+ "_onqueue_resetAndScheduleReconnect"
+ "_reconnector"
+ "gameDidBecomeForeground: %@"
+ "gameDidBecomeForeground:auditToken:"
+ "gameDidLaunch:auditToken:"
+ "initWithDisplayName:executableURL:isThirdPartyInstalled:"
+ "isLauncherAndGame"
+ "isThirdPartyInstalled"
+ "launcherBundleIdentifier"
+ "reset"
+ "scheduleReconnectOn:execute:"
+ "stateQueue"
- "Daemon connection interrupted..."
- "Daemon connection invalidated..."
- "GPGameLibrary: pong!"

```
