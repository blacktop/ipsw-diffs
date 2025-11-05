## RemoteViewServices

> `/System/Library/PrivateFrameworks/RemoteViewServices.framework/Versions/A/RemoteViewServices`

```diff

-181.0.0.0.0
-  __TEXT.__text: 0x15be4
-  __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_methlist: 0x1488
+181.1.0.0.0
+  __TEXT.__text: 0x16ea4
+  __TEXT.__auth_stubs: 0x880
+  __TEXT.__objc_methlist: 0x14b4
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__cstring: 0x6537
+  __TEXT.__gcc_except_tab: 0x350
+  __TEXT.__cstring: 0x6535
   __TEXT.__dof_RemoteVie: 0x213
-  __TEXT.__unwind_info: 0x598
+  __TEXT.__unwind_info: 0x5e0
   __TEXT.__objc_classname: 0x2a5
   __TEXT.__objc_methname: 0x3f69
   __TEXT.__objc_methtype: 0x864

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10c0
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x458
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__const: 0x750
   __AUTH_CONST.__cfstring: 0x3ac0
-  __AUTH_CONST.__objc_const: 0x2358
+  __AUTH_CONST.__objc_const: 0x2318
   __AUTH.__objc_data: 0x6e0
   __DATA.__objc_ivar: 0x1c8
   __DATA.__data: 0x68

   - /System/Library/PrivateFrameworks/CoreUI.framework/Versions/A/CoreUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6020E16B-B27F-3574-BF69-1A245DAD37F8
-  Functions: 534
-  Symbols:   1691
-  CStrings:  1897
+  UUID: F2CC3436-09C0-31F1-B881-8CF8A64A1793
+  Functions: 622
+  Symbols:   1791
+  CStrings:  1896
 
Symbols:
+ +[NSRemotePanel keyPathsForPanelSettings].cold.1
+ +[PBOXRemoteMediaBrowserPanel keyPathsForPanelSettings].cold.1
+ -[NSRVS_Deallocator addBlock:].cold.1
+ -[NSRVS_Deallocator init].cold.1
+ -[NSRemotePanel _handlePerformKeyEquivalent:].cold.1
+ -[NSRemotePanel _handleSetPresentationOptions:].cold.1
+ -[NSRemotePanel _invalidatePBOXRemotePanelSession].cold.1
+ -[NSRemotePanel _runOrderingOperationWithContext:].cold.1
+ -[NSRemotePanel _runOrderingOperationWithContext:].cold.2
+ -[NSRemotePanel _setDefaultSettings].cold.1
+ -[NSRemotePanel controller:hasWindowAvailable:].cold.1
+ -[NSRemotePanel observeValueForKeyPath:ofObject:change:context:].cold.1
+ -[NSRemotePanel observeValueForKeyPath:ofObject:change:context:].cold.2
+ -[NSRemotePanel observeValueForKeyPath:ofObject:change:context:].cold.3
+ -[NSRemotePanel serializeSettings].cold.1
+ -[NSRemotePanel serializeSettings].cold.2
+ -[NSRemotePanel sheetDidEnd:returnCode:contextInfo:].cold.1
+ -[NSRemoteServiceConnection initWithServiceConnection:endpoint:].cold.1
+ -[NSRemoteServiceEndpoint _connectionDidReceiveEvent:].cold.1
+ -[NSRemoteServiceEndpoint _connectionDidReceiveEvent:].cold.2
+ -[NSRemoteServiceEndpoint init].cold.1
+ -[NSRemoteServiceReply initWithRequest:].cold.1
+ -[NSRemoteTitlebarRenamingSession _editingDidEnd:withRequest:].cold.1
+ -[NSRemoteTitlebarRenamingSession _editingDidEndWithImmediateURLResult:withRequest:].cold.1
+ -[NSRemoteTitlebarRenamingSession _makeEndpointForWindow:controller:].cold.1
+ -[NSRemoteTitlebarRenamingSession _oldEditingDidEnd:withRequest:].cold.1
+ -[NSRemoteTitlebarRenamingSession beginWithEditingMode:editingTitle:editingRange:selectedRange:].cold.1
+ -[NSRemoteTitlebarRenamingSession beginWithEditingMode:editingTitle:editingRange:selectedRange:].cold.2
+ -[NSRemoteTitlebarRenamingSession beginWithEditingMode:editingTitle:editingRange:selectedRange:].cold.3
+ -[NSRemoteTitlebarRenamingSession beginWithEditingMode:editingTitle:editingRange:selectedRange:].cold.4
+ -[NSRemoteTitlebarRenamingSession beginWithEditingMode:editingTitle:editingRange:selectedRange:].cold.5
+ -[NSRemoteTitlebarRenamingSession controller:hasWindowAvailable:].cold.1
+ -[NSRemoteWindowController _handleModalSession:].cold.1
+ -[NSRemoteWindowController _handleModalSession:].cold.10
+ -[NSRemoteWindowController _handleModalSession:].cold.11
+ -[NSRemoteWindowController _handleModalSession:].cold.12
+ -[NSRemoteWindowController _handleModalSession:].cold.13
+ -[NSRemoteWindowController _handleModalSession:].cold.14
+ -[NSRemoteWindowController _handleModalSession:].cold.15
+ -[NSRemoteWindowController _handleModalSession:].cold.2
+ -[NSRemoteWindowController _handleModalSession:].cold.3
+ -[NSRemoteWindowController _handleModalSession:].cold.4
+ -[NSRemoteWindowController _handleModalSession:].cold.5
+ -[NSRemoteWindowController _handleModalSession:].cold.6
+ -[NSRemoteWindowController _handleModalSession:].cold.7
+ -[NSRemoteWindowController _handleModalSession:].cold.8
+ -[NSRemoteWindowController _handleModalSession:].cold.9
+ -[NSRemoteWindowController _handleRequestUpdateSharedWindowFrame:].cold.1
+ -[NSRemoteWindowController _sharedWindowShouldChange:].cold.1
+ -[NSRemoteWindowController _thisWindowShouldChange:].cold.1
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.1
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.2
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.3
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.4
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.5
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.6
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.7
+ -[NSRemoteWindowController createAccessibilityChildWindow:withStyle:].cold.8
+ -[NSRemoteWindowController findAccessibilityChildWindow:].cold.1
+ -[NSRemoteWindowController findAccessibilityChildWindow:].cold.2
+ -[NSRemoteWindowController hideSharedWindow:atLocation:].cold.1
+ -[NSSharedWindowController _handleActivateSharedWindow:].cold.1
+ -[NSSharedWindowController _handleFirstResponderActionForRequest:].cold.1
+ -[NSSharedWindowController _handleFirstResponderActionForRequest:].cold.2
+ -[NSSharedWindowController _remoteWindowShouldOrderWindow:andChangeKey:orJustOrderOut:].cold.1
+ -[NSSharedWindowController _remoteWindowShouldOrderWindow:andChangeKey:orJustOrderOut:].cold.2
+ -[NSTitlebarRenamingURLResolver findAvailableURLForFinalDisplayName:withFileSystemUniquing:].cold.1
+ -[NSTitlebarRenamingURLResolver findAvailableURLForFinalDisplayName:withFileSystemUniquing:].cold.2
+ -[NSTitlebarRenamingURLResolver findAvailableURLForFinalDisplayName:withFileSystemUniquing:].cold.3
+ -[NSTitlebarRenamingURLResolver findAvailableURLForFinalDisplayName:withFileSystemUniquing:].cold.4
+ -[NSTitlebarRenamingURLResolver localizedStringForDocumentFromUnlocalizedString:].cold.1
+ -[NSTitlebarRenamingURLResolver localizedStringForDocumentFromUnlocalizedString:].cold.2
+ -[NSTitlebarRenamingURLResolver localizedStringForDocumentFromUnlocalizedString:].cold.3
+ -[NSTitlebarRenamingURLResolver resolveFinalURLInPBOXOverwriteOK:forClientPID:andEUID:usingFinalTitle:].cold.1
+ -[NSTitlebarRenamingURLResolver resolveFinalURLInPBOXOverwriteOK:forClientPID:andEUID:usingFinalTitle:].cold.2
+ -[NSTitlebarRenamingURLResolver resolveFinalURLInPBOXOverwriteOK:forClientPID:andEUID:usingFinalTitle:].cold.3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __48-[NSRemoteWindowController _handleModalSession:]_block_invoke.cold.1
+ __50-[NSRemotePanel _runOrderingOperationWithContext:]_block_invoke.132.cold.1
+ __69-[NSRemoteTitlebarRenamingSession _makeEndpointForWindow:controller:]_block_invoke.90.cold.1
+ __RVSDocumentCachedNumberFormatter_block_invoke.cold.1
+ onDeallocPerform.cold.1
- _strcmp
CStrings:
- "v"

```
