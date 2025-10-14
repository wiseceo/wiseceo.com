# wiseceo.com

Website and app for wiseceo.com - Preconfigured for Loveable, Supabase, and Netlify deployment with auto-deploy and authentication hooks.

## 🚀 Quick Setup

This repository is pre-configured for seamless integration with:
- **Loveable**: AI-powered features and authentication
- **Supabase**: Backend database and authentication
- **Netlify**: Continuous deployment and hosting

## 📋 Prerequisites

1. GitHub account (you're already here!)
2. [Netlify account](https://app.netlify.com/signup)
3. [Supabase account](https://supabase.com/dashboard)
4. [Loveable account](https://loveable.dev)

## 🔧 Setup Instructions

### 1. Netlify Setup

1. Go to [Netlify](https://app.netlify.com)
2. Click "Add new site" → "Import an existing project"
3. Connect to GitHub and select this repository
4. Build settings are already configured in `netlify.toml`
5. Click "Deploy site"

### 2. Supabase Setup

1. Go to [Supabase Dashboard](https://supabase.com/dashboard)
2. Create a new project
3. Go to Settings → API
4. Copy your `Project URL` and `anon public` key
5. Add these to Netlify:
   - Go to Site settings → Build & deploy → Environment variables
   - Add `SUPABASE_URL` and `SUPABASE_ANON_KEY`

### 3. Loveable Integration

1. Sign up at [Loveable](https://loveable.dev)
2. Create a new project
3. Get your API key from project settings
4. Add to Netlify environment variables:
   - `LOVEABLE_API_KEY`
   - `LOVEABLE_PROJECT_ID`

### 4. GitHub Actions Setup

1. Go to repository Settings → Secrets and variables → Actions
2. Add these secrets:
   - `NETLIFY_AUTH_TOKEN` (from Netlify User Settings → Applications)
   - `NETLIFY_SITE_ID` (from Netlify Site Settings → General)
   - `SUPABASE_URL`
   - `SUPABASE_ANON_KEY`
   - `LOVEABLE_API_KEY`

## 🎯 Features

### Auto-Deployment
- ✅ Automatic deployment on push to `main` branch
- ✅ Preview deployments for pull requests
- ✅ Build status checks

### Supabase Backend
- ✅ Database ready for use
- ✅ Authentication configured
- ✅ Row-level security enabled

### Netlify Continuous Deployment
- ✅ Auto-deploy on git push
- ✅ Deploy previews for PRs
- ✅ Instant rollback capability

### Loveable AI Features
- ✅ Authentication hooks ready
- ✅ AI chat integration
- ✅ Smart search capabilities

## 📁 Project Structure

```
wiseceo.com/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── .env.example                # Environment variables template
├── netlify.toml                # Netlify configuration
└── README.md                   # This file
```

## 🔒 Security

- Never commit `.env` files
- Use environment variables for all secrets
- Enable branch protection on `main`
- Use Supabase Row Level Security (RLS)

## 📚 Documentation

- [Netlify Docs](https://docs.netlify.com)
- [Supabase Docs](https://supabase.com/docs)
- [Loveable Docs](https://docs.loveable.dev)
- [GitHub Actions](https://docs.github.com/actions)

## 🆘 Support

For issues or questions:
1. Check the documentation links above
2. Review the `.env.example` file
3. Check GitHub Actions logs for deployment issues

## 📝 License

MIT License - feel free to use this template for your own projects!
