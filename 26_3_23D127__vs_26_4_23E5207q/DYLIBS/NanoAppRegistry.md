## NanoAppRegistry

> `/System/Library/PrivateFrameworks/NanoAppRegistry.framework/NanoAppRegistry`

```diff

 71.0.4.0.0
-  __TEXT.__text: 0x2214
-  __TEXT.__auth_stubs: 0x260
+  __TEXT.__text: 0x2554
+  __TEXT.__auth_stubs: 0x220
   __TEXT.__objc_methlist: 0x57c
   __TEXT.__cstring: 0x251
   __TEXT.__const: 0x10
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0x140
+  __TEXT.__unwind_info: 0x170
   __TEXT.__objc_classname: 0x91
   __TEXT.__objc_methname: 0xd6f
   __TEXT.__objc_methtype: 0x271

   __DATA_CONST.__objc_selrefs: 0x3b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__auth_got: 0x120
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0x340
   __AUTH_CONST.__objc_const: 0xbc8

   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9227A91B-0E5A-33C6-9920-343762E53AAF
+  UUID: 5060DA39-BF4A-3DBD-ABCD-7BE90A0D45E4
   Functions: 106
-  Symbols:   458
+  Symbols:   454
   CStrings:  284
 
Symbols:
+ _objc_retain
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[NARGlance encodeWithCoder:] : 236 -> 252
~ -[NARGlance initWithCoder:] : 340 -> 360
~ -[NARGlance description] : 132 -> 140
~ -[NARGlance debugDescription] : 140 -> 148
~ ___41-[NARApplicationWorkspace workspaceInfo:]_block_invoke : 236 -> 240
~ ___41-[NARApplicationWorkspace workspaceInfo:]_block_invoke_2 : 16 -> 72
~ ___41-[NARApplicationWorkspace workspaceInfo:]_block_invoke_3 : 16 -> 72
~ -[NARApplicationWorkspace getWorkspaceInfoWithCompletion:] : 184 -> 188
~ ___58-[NARApplicationWorkspace getWorkspaceInfoWithCompletion:]_block_invoke : 260 -> 272
~ -[NARApplicationWorkspace getWorkspaceInfoIncludingHiddenApps:completion:] : 192 -> 196
~ ___74-[NARApplicationWorkspace getWorkspaceInfoIncludingHiddenApps:completion:]_block_invoke : 276 -> 280
~ -[NARApplicationWorkspace _connectionInvalidated] : 136 -> 140
~ -[NARApplicationWorkspace _loadConnectionIfNeeded] : 292 -> 296
~ -[NARApplicationWorkspace setConnection:] : 12 -> 64
~ -[NARApplicationWorkspace setQueue:] : 12 -> 64
~ _nar_sync_log : 68 -> 84
~ _nar_workspace_log : 68 -> 84
~ -[NARWorkspaceInfo initWithCoder:] : 296 -> 312
~ -[NARWorkspaceInfo encodeWithCoder:] : 128 -> 136
~ -[NARWorkspaceInfo initWithApplications:UUID:sequenceNumber:] : 188 -> 172
~ -[NARApplicationState encodeWithCoder:] : 108 -> 116
~ -[NARApplication initWithCoder:] : 492 -> 524
~ ___32-[NARApplication initWithCoder:]_block_invoke : 236 -> 240
~ -[NARApplication encodeWithCoder:] : 288 -> 300
~ -[NARApplication applicationIdentifier] : 88 -> 96
~ -[NARApplication bundleName] : 88 -> 96
~ -[NARApplication localizedBundleNames] : 200 -> 204
~ ___38-[NARApplication localizedBundleNames]_block_invoke : 124 -> 128
~ -[NARApplication bundleVersion] : 88 -> 96
~ -[NARApplication localizedDisplayName] : 436 -> 504
~ -[NARApplication localizedDisplayNames] : 200 -> 204
~ ___39-[NARApplication localizedDisplayNames]_block_invoke : 124 -> 128
~ -[NARApplication vendorName] : 88 -> 96
~ -[NARApplication itemName] : 88 -> 96
~ -[NARApplication supportedSchemes] : 88 -> 96
~ -[NARApplication localizations] : 76 -> 84
~ -[NARApplication objectForInfoDictionaryKey:] : 108 -> 116
~ -[NARApplication objectForInfoDictionaryKey:localization:] : 148 -> 156
~ -[NARApplication description] : 200 -> 216
~ -[NARApplication setAppTags:] : 12 -> 64
~ -[NARApplication setAppState:] : 12 -> 64
~ -[NARApplication setInfoPlist:] : 12 -> 64
~ -[NARApplication setLocalizedStrings:] : 12 -> 64
~ -[NARApplication setITunesPlistStrings:] : 12 -> 64

```
