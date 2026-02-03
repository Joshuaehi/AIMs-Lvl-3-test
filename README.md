# Alberta Design System - Pixel-Perfect HTML Template

This directory contains a pixel-perfect recreation of the Alberta Design System basic page layout.

## Files Created

### 1. `alberta-design-system.html` (13KB)
The main HTML file that replicates the structure and layout of the Alberta Design System documentation site. It includes:
- Complete page structure using GOA (Government of Alberta) web components
- Microsite header with Alberta government branding
- App header with navigation
- Side menu navigation
- Main content area with examples
- Footer with navigation sections
- Responsive design that works on desktop, tablet, and mobile

### 2. `alberta-design-system.css` (14KB)
Comprehensive CSS file with:
- All design tokens (colors, typography, spacing, shadows)
- Font imports (Roboto Mono, acumin-pro-semi-condensed)
- Layout styles for responsive grid
- Component-specific styling
- Responsive breakpoints for tablet (max-width: 1231px) and mobile (max-width: 896px, 623px)
- Accessibility features (focus states, skip links)
- Print styles

### 3. `alberta.svg` (550 bytes)
Placeholder SVG logo for the Alberta government. **Replace this with the official Alberta logo** when available.

## Usage

### Option 1: Open Directly in Browser
Simply open `alberta-design-system.html` in a web browser. The file references:
- GOA web components from CDN (jsDelivr)
- Ionicons for icon support
- Local CSS file (`alberta-design-system.css`)

### Option 2: Serve with Local Web Server
For best results, serve the files through a local web server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js (http-server)
npx http-server

# Using PHP
php -S localhost:8000
```

Then visit: `http://localhost:8000/alberta-design-system.html`

## Customization

### Replace the Logo
Replace `alberta.svg` with the official Alberta government logo. The logo should be:
- Approximately 120px wide × 44px height
- SVG format (preferred) or PNG
- Optimized for web use

### Modify Content
Edit the HTML file to change:
- Page title and headings
- Navigation menu items
- Main content sections
- Footer links

### Adjust Styling
Edit the CSS file to customize:
- Colors (search for `--goa-color-*` variables)
- Typography (search for `--goa-typography-*` variables)
- Spacing (search for `--goa-space-*` variables)
- Component-specific styles

## Component Library

The HTML uses the official GOA Web Components library from:
- **Package**: `@abgov/web-components@1.34.0`
- **CDN**: jsDelivr
- **Documentation**: https://design.alberta.ca
- **GitHub**: https://github.com/GovAlta/ui-components

### Available Components Used
- `<goa-one-column-layout>` - Main page layout
- `<goa-microsite-header>` - Government header banner
- `<goa-app-header>` - Application header with logo and navigation
- `<goa-app-header-menu>` - Header navigation menu
- `<goa-side-menu>` - Side navigation
- `<goa-side-menu-group>` - Collapsible side menu sections
- `<goa-text>` - Typography component
- `<goa-container>` - Content container
- `<goa-callout>` - Important message boxes
- `<goa-notification>` - Banner notifications
- `<goa-icon>` - Icon component
- `<goa-icon-button>` - Icon button with tooltip support
- `<goa-popover>` - Dropdown/popover menus
- `<goa-tooltip>` - Contextual help tooltips
- `<goa-divider>` - Visual separators
- `<goa-app-footer>` - Application footer
- `<goa-app-footer-nav-section>` - Footer navigation sections
- `<goa-app-footer-meta-section>` - Footer metadata section

## Browser Support

The design system supports all modern browsers:
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

Web Components require modern browser support. For older browsers, you may need polyfills.

## Responsive Breakpoints

The layout adapts at these breakpoints:
- **Desktop**: 1232px and above (full layout with side menu)
- **Tablet**: 897px - 1231px (condensed spacing)
- **Mobile**: 896px and below (stacked layout, collapsed menu)
- **Small Mobile**: 623px and below (mobile typography)

## Design Tokens

All design tokens are defined as CSS custom properties in the `:root` selector. Key token categories:
- **Typography**: Font sizes (1-10), weights, line heights
- **Colors**: Greyscale, brand, interactive, text colors
- **Spacing**: 4xs to 4xl (2px to 128px)
- **Shadows**: 6 levels (150-600)
- **Icons**: Size tokens for small, medium, large

## Accessibility

The template includes:
- Semantic HTML5 elements
- ARIA labels and roles
- Keyboard navigation support
- Focus indicators
- Screen reader friendly structure
- Color contrast compliance

## Sources

This template was created based on:
- [Alberta Design System](https://design.alberta.ca/)
- [GOA UI Components on GitHub](https://github.com/GovAlta/ui-components)
- [@abgov/web-components on npm](https://www.npmjs.com/package/@abgov/web-components)
- [Alberta Government Identity Program](https://www.alberta.ca/government-identity-program)
- [Design Standards Checklist](https://www.alberta.ca/design-standards-checklist-resources)

## Next Steps

1. **Replace the logo**: Update `alberta.svg` with the official logo
2. **Update content**: Modify the HTML to match your application's content
3. **Customize colors**: Adjust CSS variables to match your branding (if needed)
4. **Add functionality**: Add JavaScript for interactive features
5. **Test responsiveness**: Verify layout on different screen sizes
6. **Validate accessibility**: Run accessibility audits using tools like Lighthouse

## License

This template is based on the Government of Alberta Design System. Please refer to the official design system documentation for usage guidelines and licensing information.

## Support

For questions about the Alberta Design System:
- Visit: https://design.alberta.ca/support
- GitHub Issues: https://github.com/GovAlta/ui-components/issues
- Slack: #design-system-support
