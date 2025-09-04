## Frontend - YC Crap Analysis

This is the Next.js frontend for the YC Crap Analysis project. It provides a user interface for analyzing YC startups and visualizing results from the backend.

---

### Roadmap / Step-by-Step Guide

#### 1. Project Setup
- [ ] Install [Node.js LTS](https://nodejs.org/en/download/)
- [ ] Install dependencies: `npm install`
- [ ] Review [Next.js project structure](https://nextjs.org/docs/app/building-your-application/routing)

#### 2. UI/UX Design
- [ ] Sketch wireframes (use [Figma Free](https://www.figma.com/) or [Excalidraw](https://excalidraw.com/)) for:
	- Home page (input YC startup, see results)
	- Results page (show analysis, charts, risk score)
	- About page (explain project purpose)
- [ ] Choose a UI library:
	- [Tailwind CSS](https://tailwindcss.com/docs/guides/nextjs) (recommended)
	- [Chakra UI](https://chakra-ui.com/getting-started)
- [ ] Implement responsive layout (see [Tailwind Responsive Design](https://tailwindcss.com/docs/responsive-design))

#### 3. API Integration
- [ ] Define API endpoints (see backend/README.md)
- [ ] Create API utility functions using [fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) or [Axios](https://axios-http.com/docs/intro)
- [ ] Handle loading, error, and success states in UI (see [React Error Boundaries](https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary))

#### 4. Features Implementation
- [ ] Input form for startup name/URL (see [React Forms](https://react.dev/learn/sharing-state-between-components#passing-data-deeply-with-context))
- [ ] Display analysis results (risk score, explanation, charts)
	- Use [Recharts](https://recharts.org/en-US/) or [Chart.js](https://www.chartjs.org/docs/latest/) for charts
- [ ] Add helpful tooltips and documentation in UI (see [Radix UI Tooltip](https://www.radix-ui.com/primitives/docs/components/tooltip))
- [ ] (Optional) User authentication with [NextAuth.js](https://next-auth.js.org/getting-started/introduction)

#### 5. Testing
- [ ] Write unit tests for components using [Jest](https://jestjs.io/docs/getting-started) and [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [ ] Test API integration (mock backend responses with [msw](https://mswjs.io/))

#### 6. Deployment
- [ ] Deploy to [Vercel](https://vercel.com/docs/concepts/projects/overview) (free tier is sufficient)
- [ ] Set up environment variables for API URLs ([Vercel Env Vars](https://vercel.com/docs/concepts/projects/environment-variables))
- [ ] Test production build: `npm run build && npm start`

#### 7. Documentation
- [ ] Write clear usage instructions (see [README best practices](https://www.makeareadme.com/))
- [ ] Add screenshots/gifs of the UI ([Licecap](https://www.cockos.com/licecap/) for gifs)

---

### Resources for Beginners
- [Next.js Documentation](https://nextjs.org/docs)
- [React Docs](https://react.dev/learn)
- [Vercel Deployment Guide](https://vercel.com/docs)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [API Integration in Next.js](https://nextjs.org/docs/pages/building-your-application/data-fetching)

---

See the main project README for the overall roadmap and backend/README.md for backend steps.
