## MobileSafariUI

> `/System/Library/PrivateFrameworks/MobileSafariUI.framework/MobileSafariUI`

```diff

-621.3.7.10.1
-  __TEXT.__text: 0x1d5430
+621.3.8.0.0
+  __TEXT.__text: 0x1d58e4
   __TEXT.__auth_stubs: 0x1e40
   __TEXT.__objc_methlist: 0x2003c
   __TEXT.__const: 0x71a
-  __TEXT.__gcc_except_tab: 0x1a950
-  __TEXT.__cstring: 0xc23b
+  __TEXT.__gcc_except_tab: 0x1a944
+  __TEXT.__cstring: 0xc64b
   __TEXT.__dlopen_cstrs: 0x774
   __TEXT.__oslogstring: 0x8cfe
   __TEXT.__ustring: 0x10f6

   __TEXT.__unwind_info: 0xbd80
   __TEXT.__eh_frame: 0x2d8
   __TEXT.__objc_classname: 0x3dd9
-  __TEXT.__objc_methname: 0x65c8a
+  __TEXT.__objc_methname: 0x65ca3
   __TEXT.__objc_methtype: 0x1453b
   __TEXT.__objc_stubs: 0x438a0
-  __DATA_CONST.__got: 0x26b8
+  __DATA_CONST.__got: 0x26c0
   __DATA_CONST.__const: 0x8110
   __DATA_CONST.__objc_classlist: 0x850
   __DATA_CONST.__objc_catlist: 0xa8

   __DATA_CONST.__objc_arraydata: 0x270
   __AUTH_CONST.__auth_got: 0xf38
   __AUTH_CONST.__const: 0x2d18
-  __AUTH_CONST.__cfstring: 0xb7e0
-  __AUTH_CONST.__objc_const: 0x2cb88
+  __AUTH_CONST.__cfstring: 0xb9e0
+  __AUTH_CONST.__objc_const: 0x2cba8
   __AUTH_CONST.__objc_intobj: 0x468
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x240
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x1b98
   __AUTH.__data: 0x80
-  __DATA.__objc_ivar: 0x1fbc
+  __DATA.__objc_ivar: 0x1fc0
   __DATA.__data: 0x7360
   __DATA.__bss: 0x4f0
   __DATA.__common: 0x10

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: C36B576A-BEBE-3848-85D7-8BED33423A7B
+  UUID: 1E7309DC-087C-3624-913D-E399D74A6E1F
   Functions: 11056
-  Symbols:   41646
-  CStrings:  20521
+  Symbols:   41648
+  CStrings:  20554
 
Symbols:
+ _OBJC_IVAR_$_BrowserWindowController._cloudTabRestorationLogs
+ __SFCloudTabsDeviceUUIDForRestorationDebugSyncLogDefaultsKey
+ ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke.59
+ ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke.63
+ ___52-[BrowserWindowController windowForSceneID:options:]_block_invoke.94
+ ___62-[BrowserWindowController _mergeWindowStates:intoWindowState:]_block_invoke.117
+ ___71-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestoration:]_block_invoke.78
+ ___block_descriptor_56_e8_32s40s48s_e21_B16?0"WBSCloudTab"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56r_e8_v12?0B8ls32l8s40l8r56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8s40l8s48l8s56l8
+ ___block_literal_global.113
+ ___block_literal_global.96
- ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke.28
- ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke.29
- ___52-[BrowserWindowController windowForSceneID:options:]_block_invoke.45
- ___62-[BrowserWindowController _mergeWindowStates:intoWindowState:]_block_invoke.68
- ___71-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestoration:]_block_invoke.35
- ___block_descriptor_48_e8_32s40s_e21_B16?0"WBSCloudTab"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e8_v12?0B8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e41_v32?0"NSString"8"NSMutableArray"16^B24ls32l8s40l8s48l8
- ___block_literal_global.47
- ___block_literal_global.71
Functions (modified):
~ -[BrowserWindowController initWithTabGroupManager:browserState:pinnedTabsManager:perSitePreferencesVendor:shouldMergeAllWindowsIfNeeded:browserControllerUIDelegateProvider:] : 496 -> 524
~ -[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:] : 2176 -> 2820
~ -[BrowserWindowController initWithBrowserSavedState:perSitePreferencesVendor:browserControllerUIDelegateProvider:] : 360 -> 388
~ ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke : 148 -> 208
~ -[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestoration:] : 1436 -> 1536
~ ___71-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestoration:]_block_invoke : 436 -> 632

Functions (added):
+ ___108-[BrowserWindowController _mergeTabsFromCloudTabsForDeviceRestorationIfNeededAfterCloudTabsFinishedSyncing:]_block_invoke.59

Functions (removed):
- -[BrowserWindowController .cxx_destruct]
CStrings:
+ "Attempting to find device with UUID: %@ to restore from. Current CloudTab device UUID is: %@"
+ "Did not find browser controller for scene ID %@, falling back to the first one"
+ "Finished syncing for CloudTabs restoration (saved UUID: %@, current UUID: %@)"
+ "Found CloudTabs device with UUID %@"
+ "No cloud tab device found for tab restoration. Expected device %@ to have %zu tabs as of %@."
+ "No tab was found for merging from a CloudTabs device with UUID %@"
+ "_cloudTabRestorationLogs"

```
