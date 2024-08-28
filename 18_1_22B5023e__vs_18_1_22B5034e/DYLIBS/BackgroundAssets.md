## BackgroundAssets

> `/System/Library/Frameworks/BackgroundAssets.framework/BackgroundAssets`

```diff

-180.0.0.0.0
+182.0.0.0.0
   __TEXT.__text: 0x11a6c
   __TEXT.__auth_stubs: 0x7f0
   __TEXT.__objc_methlist: 0xabc
   __TEXT.__const: 0x288
   __TEXT.__gcc_except_tab: 0x360
-  __TEXT.__cstring: 0x3283
+  __TEXT.__cstring: 0x32b3
   __TEXT.__oslogstring: 0x4d4
   __TEXT.__swift5_typeref: 0x168
   __TEXT.__swift5_fieldmd: 0x64
CStrings:
+ "BUG IN CLIENT OF BackgroundAssets: Calling `startForegroundDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyAsNonEssential]` (removingEssential in Swift) first."
+ "Calling `startForegroundDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyAsNonEssential]` (removingEssential in Swift) first."
+ "BUG IN CLIENT OF BackgroundAssets: Calling `scheduleDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyAsNonEssential]` (removingEssential in Swift) first."
+ "Calling `scheduleDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyAsNonEssential]` (removingEssential in Swift) first."
- "Calling `scheduleDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyWithDownloadNecessityOptional]` first."
- "BUG IN CLIENT OF BackgroundAssets: Calling `startForegroundDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyWithDownloadNecessityOptional]` first."
- "Calling `startForegroundDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyWithDownloadNecessityOptional]` first."
- "BUG IN CLIENT OF BackgroundAssets: Calling `scheduleDownload:error:` with an `Essential` necessity is prohibited. Call `[BADownload copyWithDownloadNecessityOptional]` first."

```
