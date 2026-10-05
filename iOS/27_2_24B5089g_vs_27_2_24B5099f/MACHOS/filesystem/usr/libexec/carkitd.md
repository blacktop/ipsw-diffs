## carkitd

> `/usr/libexec/carkitd`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__TEXT.__oslogstring`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA.__objc_const`

```diff

-807.2.0.0.0
+807.4.0.0.0
   __TEXT.__text: 0x93e78
   __TEXT.__auth_stubs: 0x18f0
   __TEXT.__objc_stubs: 0x118a0
CStrings:
+ "PrivateFrameworks/CarPlayAsset.framework"
+ "failed to find CarPlayAsset.framework"
+ "no MaximumAssetCompatibilityVersion in CarPlayAsset.framework"
- "PrivateFrameworks/CarPlayAssetUI.framework"
- "failed to find CarPlayAssetUI.framework"
- "no MaximumAssetCompatibilityVersion in CarPlayAssetUI.framework"
```
