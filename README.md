# ipsw-diffs

> IPSW Diffs

---

## DIFFS

### iOS 17.6.1

- [17.6 beta 1 (21G5052e) .vs 17.6 beta 2 (21G5061c)](17_6_21G5052e__vs_17_6_21G5061c/TOC.md)
- [17.6 beta 2 (21G5061c) .vs 17.6 beta 3 (21G5066d)](17_6_21G5061c__vs_17_6_21G5066d/TOC.md)

### iOS 18.0 beta

- [17.5.1 (21F90) .vs 18.0 beta 1 (22A5282m)](17_5_1_21F90__vs_18_0_22A5282m/TOC.md)
- [18.0 beta 1 (22A5282m) .vs 18.0 beta 2 (22A5297f)](18_0_22A5282m__vs_18_0_22A5297f/TOC.md)
- [18.0 beta 2 (22A5297f) .vs 18.0 beta 3 (22A5307f)](18_0_22A5297f__vs_18_0_22A5307f/TOC.md)

### Generating Diffs

```bash
ipsw diff 
  --output '../ipsw-diffs'
  --markdown 
  --fw 
  --launchd
  --feat
  'iPhone16,2_17.6_21G5052e_Restore.ipsw'
  'iPhone16,2_17.6_21G5061c_Restore.ipsw'
  --kdk '/Library/Developer/KDKs/KDK_14.6_23G5052d.kdk/System/Library/Kernels/kernel.release.t6031' 
  --kdk '/Library/Developer/KDKs/KDK_14.6_23G5061b.kdk/System/Library/Kernels/kernel.release.t6031'
```
> [!NOTE]  
> DIFFs generated via [`ipsw diff`](https://blacktop.github.io/ipsw/docs/cli/ipsw/diff/#ipsw-diff)

## PRs Welcome

Have a diff that you think others would be interested in? Run the above command and create a PR to add it here!

## License

MIT Copyright (c) 2024 **blacktop**